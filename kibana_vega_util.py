import json
import requests

with open('config.json') as config_file:
  es_config = json.load(config_file)


def saveVegaLiteVis(index, visName, altairChart, resultSize=100, timeField="timestamp", verify=True):
    chart_json = json.loads(altairChart.to_json())
    chart_json['data']['url'] = {
        "%context%": True,
        "index": index,
        "body": {
            "size": resultSize
        }
    }

    if timeField:
      chart_json['data']['url']['%timefield%'] = timeField

    visState = {
      "type": "vega",
      "aggs": [],
      "params": {
        "spec": json.dumps(chart_json, sort_keys=True, indent=4, separators=(',', ': ')),
      },
      "title": visName
    }

    visSavedObject={
      "attributes" : {
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
      }
    }

    return requests.post(
        es_config['kibana_client'] + '/api/saved_objects/visualization/' + visName,
        json=visSavedObject,
        auth=(es_config['user'], es_config['password']),
        headers={"kbn-xsrf":"jupyter2kibana"},
        verify=verify
    )

def saveVegaVis(index, visName, altairChart, resultSize=100, timeField="timestamp", verify=True):
    chart_json = json.loads(altairChart.to_json())
    chart_json['spec']['data']['url'] = {
        "%context%": True,
        "index": index,
        "body": {
            "size": resultSize
        }
    }

    if timeField:
      chart_json['spec']['data']['url']['%timefield%'] = timeField

    visState = {
      "type": "vega",
      "aggs": [],
      "params": {
        "spec": json.dumps(chart_json, sort_keys=True, indent=4, separators=(',', ': ')),
      },
      "title": visName
    }

    visSavedObject={
        "attributes" : {
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
    }

    return requests.post(
        es_config['kibana_client'] + '/api/saved_objects/visualization/' + visName,
        json=visSavedObject,
        auth=(es_config['user'], es_config['password']),
        headers={"kbn-xsrf":"jupyter2kibana"},
        verify=verify
    )

