const http = require("http");
const httpProxy = require("http-proxy");

const config = require("./config.json");

//
// Create your proxy server and set the target in the options.
//
const proxy = httpProxy.createProxyServer({});

var sendError = function (res, err) {
  return res.status(500).send({
    error: err,
    message: "An error occured in the proxy",
  });
};

// error handling
proxy.on("error", function (err, req, res) {
  sendError(res, err);
});

var enableCors = function (req, res) {
  if (req.headers["access-control-request-method"]) {
    res.setHeader(
      "access-control-allow-methods",
      req.headers["access-control-request-method"]
    );
  }

  if (req.headers["access-control-request-headers"]) {
    res.setHeader(
      "access-control-allow-headers",
      req.headers["access-control-request-headers"]
    );
  }

  if (req.headers.origin) {
    res.setHeader("access-control-allow-origin", req.headers.origin);
    res.setHeader("access-control-allow-credentials", "true");
  }
};

// set header for CORS
proxy.on("proxyRes", function (proxyRes, req, res) {
  enableCors(req, res);
});

var server = http.createServer(function (req, res) {
  // You can define here your custom logic to handle the request
  // and then proxy the request.
  if (req.method === "OPTIONS") {
    enableCors(req, res);
    res.writeHead(200);
    res.end();
    return;
  }

  proxy.web(
    req,
    res,
    {
      target: `https://localhost:9200`,
      auth: `${config.user}:${config.password}`,
      ssl: false,
      secure: false,
      changeOrigin: true,
    },
    function (err) {
      sendError(res, err);
    }
  );
});

server.listen(9220);
