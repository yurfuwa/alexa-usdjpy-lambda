import sys
import os
import json
import requests
import echokit

handler = echokit.handler
echokit.application_id = os.environ['APP_ID']
echokit.verify_application_id = False

@echokit.on_session_launch
def session_started(request_wrapper):
    return echokit.ask('Hello!')

@echokit.on_session_ended
def session_ended(request_wrapper):
    # Print statement will log the reason to CloudWatch
    print(request_wrapper.request.reason)

@echokit.on_intent('UsdJpy')
def usd_jpy(request):
    req = requests.get('https://www.gaitameonline.com/rateaj/getrate')
    j = req.json()
    res = None

    for item in j['quotes']:
        if item['currencyPairCode'] == "USDJPY":
            res = item['ask']
            print(res)

    return echokit.tell("USDJPY rate is {} yen".format(res))

#  @echokit.on_intent('OrderIntent')
#  @echokit.slot('MenuItem', dest='menu_item')
#  def order_intent(request_wrapper, menu_item):
    #  print(menu_item)
    #  request = request_wrapper.request
    #  menu_item = request.intent.slots['MenuItem'].value
    #  return echokit.tell(f"You just ordered {menu_item}")\
    #  .simple_card(title="Previous order", content=menu_item)



