from obswebsocket import obsws, requests
from pythonosc import dispatcher
from pythonosc import osc_server

# OBS OSC Creds
obsws_host = "localhost"
obsws_port = 4444
obsws_password = "secret"

obs_ws = obsws(obsws_host, obsws_port, obsws_password)
obs_ws.connect()

# OSC Server Creds
osc_host = "0.0.0.0"  # expose it to the network
osc_port = 5005

scenes_names = []


def index_scenes():
    scenes = obs_ws.call(requests.GetSceneList())
    for scene in scenes.getScenes():
        name = scene["name"]
        scenes_names.append(name)


def scene_preview(unused, args, scene_idx: int):
    """ select scene to preview """
    scene = scenes_names[scene_idx]
    obs_ws.call(requests.SetPreviewScene(scene))


def scene_pgm(unsused, args, scene_idx: int):
    """ sends scene from preview into pgm """
    scene = scenes_names[scene_idx]
    obs_ws.call(requests.SetCurrentScene(scene))


def go_transition(unsused, args, transition):
    """ set a custom transition on scene in preview """
    obs_ws.call(requests.SetCurrentTransition(transition))
    obs_ws.call(requests.TransitionToProgram(transition))


if __name__ == "__main__":
    index_scenes()
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/osc/scene/preview", scene_preview, "")
    dispatcher.map("/osc/scene/program", scene_pgm, "")
    dispatcher.map("/osc/scene/transition", go_transition, "")

    server = osc_server.ThreadingOSCUDPServer((osc_host, osc_port), dispatcher)
    print(f"Serving on {server.server_address}")
    server.serve_forever()
