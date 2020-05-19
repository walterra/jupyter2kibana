import datetime
import json

def saveVegaLiteVis(client, index, visName, altairChart, resultSize=100, timeField=True):
    chart_json = json.loads(altairChart.to_json())
    chart_json['data']['url'] = {
        "%context%": True,
        "index": index,
        "body": {
            "size": resultSize
        }
    }

    if timeField:
      chart_json['data']['url']['%timefield%'] = "timestamp"

    visState = {
      "type": "vega",
      "aggs": [],
      "params": {
        "spec": json.dumps(chart_json, sort_keys=True, indent=4, separators=(',', ': ')),
      },
      "title": visName
    }

    visSavedObject={
        "visualization" : {
          "title" : visName,
          "visState" : json.dumps(visState, sort_keys=True, indent=4, separators=(',', ': ')),
          "uiStateJSON" : "{}",
          "description" : "",
          "version" : 1,
          "kibanaSavedObjectMeta" : {
            "searchSourceJSON" : json.dumps({
              "query": {
                "language": "kuery",
                "query": ""
              },
              "filter": []
            }),
          }
        },
        "type" : "visualization",
        "references" : [ ],
        "migrationVersion" : {
          "visualization" : "7.7.0"
        },
        "updated_at" : datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")
    }

    return client.index(index='.kibana',id='visualization:'+visName,body=visSavedObject)

def saveVegaVis(client, index, visName, altairChart, resultSize=100, timeField=True):
    chart_json = json.loads(altairChart.to_json())
    chart_json['spec']['data']['url'] = {
        "%context%": True,
        "index": index,
        "body": {
            "size": resultSize
        }
    }

    if timeField:
      chart_json['spec']['data']['url']['%timefield%'] = "timestamp"

    visState = {
      "type": "vega",
      "aggs": [],
      "params": {
        "spec": json.dumps(chart_json, sort_keys=True, indent=4, separators=(',', ': ')),
      },
      "title": visName
    }

    visSavedObject={
        "visualization" : {
          "title" : visName,
          "visState" : json.dumps(visState, sort_keys=True, indent=4, separators=(',', ': ')),
          "uiStateJSON" : "{}",
          "description" : "",
          "version" : 1,
          "kibanaSavedObjectMeta" : {
            "searchSourceJSON" : json.dumps({
              "query": {
                "language": "kuery",
                "query": ""
              },
              "filter": []
            }),
          }
        },
        "type" : "visualization",
        "references" : [ ],
        "migrationVersion" : {
          "visualization" : "7.7.0"
        },
        "updated_at" : datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")
    }

    return client.index(index='.kibana',id='visualization:'+visName,body=visSavedObject)
