# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# -*- coding: utf-8 -*-

import http.client, urllib.parse, json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.
subscriptionKey = "51f8aeba411e4e86b358d5bb2d998aed"


host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/search"

term = "election language:en location:us site:twitter.com"
date_time = "2012-01-16..2012-01-20"


def BingWebSearch(search, dtime):
    """Performs a Bing Web search and returns the results."""

    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    # + "?year=" + "1" + "?mkt=" + "en-GB"
    query = urllib.parse.quote(search, dtime)
    conn.request("GET", path + "?q=" + query + "&year=", headers=headers)
    response = conn.getresponse()
    headers = [k + ": " + v for (k, v) in response.getheaders()
               if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
    return headers, response.read().decode("utf8")


if len(subscriptionKey) == 32:
    print('Searching the Web for: ', term)
    headers, result = BingWebSearch(term, date_time)
    print("\nRelevant HTTP Headers:\n")
    print("\n".join(headers))
    print("\nJSON Response:\n")
    resultjson = json.loads(result)
    print(resultjson)
    with open('snippet_twitter.txt', 'w', encoding="utf-8") as f:
        for i in range(0, 10):
            f.writelines(resultjson['webPages']['value'][i]['snippet']+'\n')
            print(resultjson['webPages']['value'][i]['snippet'])
else:

    print("Invalid Bing Search API subscription key!")
    print("Please paste yours into the source code.")