#!/bin/bash

docker tag joshsalvia/webprojectone registry.heroku.com/$HEROKU_APP_NAME/web
docker push joshsalvia/webprojectone
docker push registry.heroku.com/$HEROKU_APP_NAME/web
heroku container:release web --app $HEROKU_APP_NAME