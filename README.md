# Alexa-USDJPY-Lambda

just say `Alexa , tell me USDJPY`

## required

* docker
* amazon account



## what's alexa and skill

* https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function
* https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interface-reference

## how to development alexa custom skill and lambda

* http://qiita.com/sparkgene/items/ac3d14f1e8815ce8802a
* http://qiita.com/sawanoboly/items/0981502ab66e975f64a6
* http://qiita.com/Hironsan/items/0eb5578f3321c72637b4
* https://github.com/arcward/echokit
  * http://echokit.readthedocs.io/en/latest/
  * https://github.com/arcward/echokit-example/blob/master/order_skill/order_skill.py
      * +warning+ , this example is old syntax.
      * you not need to `from echokit import Response, PlainTextOutputSpeech, SimpleCard`
      * you need `echokit.verify_application_id = False`


## Installation for development

* `docker build -t alexa-lambda:latest ./`
* `docker run -it --rm -v "$PWD":/usr/src/app -w /usr/src/app alexa-lambda:latest python script.py`

## Build for development

* ` docker cp {CONTAINER_ID}:/usr/src/app/ ./build/`
   * Lambda need all dependent files in one dir.
* `cd ./build && zip -r ../upload.zip *`
   * Lambda need upload zip file for package.

