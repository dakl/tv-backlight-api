# Development

## Run locally

~~~bash
python run.py
~~~

# Deplotyment

## Build & push

~~~bash
docker build -t dakl/tv-backlight-api .
docker push dakl/tv-backlight-api
~~~

## Run Container

~~~bash
docker run \
-e RELAY_HUB_DEVICE_ID=(echo $RELAY_HUB_DEVICE_ID) \
-e LEGO_HOUSE_DEVICE_ID=(echo $LEGO_HOUSE_DEVICE_ID) \
-e PARTICLE_ACCESS_TOKEN=(echo $PARTICLE_ACCESS_TOKEN) \
-p 8000:8000 \
dakl/tv-backlight-api
~~~

## Run in swarm

~~~bash
docker service create \
--replicas 1 \
--name tv-backlight-api \
-e RELAY_HUB_DEVICE_ID=(echo $RELAY_HUB_DEVICE_ID) \
-e LEGO_HOUSE_DEVICE_ID=(echo $LEGO_HOUSE_DEVICE_ID) \
-e PARTICLE_ACCESS_TOKEN=(echo $PARTICLE_ACCESS_TOKEN) \
-p 8000:8000 \
dakl/tv-backlight-api
~~~

# CI
Should build and push image. TBD.
