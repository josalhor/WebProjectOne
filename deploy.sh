#!/bin/sh

docker tag joshsalvia/webprojectone registry.heroku.com/$HEROKU_APP_NAME/web
docker push joshsalvia/webprojectone
docker push registry.heroku.com/$HEROKU_APP_NAME/web
echo "${HEROKU_USERNAME}\n${HEROKU_TOKEN}" | heroku login -i 
heroku container:release web --app $HEROKU_APP_NAME