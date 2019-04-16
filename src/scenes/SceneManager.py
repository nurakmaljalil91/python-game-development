class SceneManager:
    def __init__(self):
        self.scenes = []

    def is_empty(self):
        return self.scenes == []

    def push(self, scene):
        self.scenes.append(scene)
        self.current_scene_number = len(self.scenes) - 1

    def pop(self):
        return self.scenes.pop()

    def peek(self):
        return self.scenes[len(self.scenes) - 1]

    def size(self):
        return len(self.scenes)

    def set_current_scene(self, scene):
        self.scenes.pop()
        self.scenes.push(scene)

    def current_scene(self, scene_number):
        self.current_scene_number = scene_number
        return self.scenes[scene_number]

    def get_current_scene_number(self):
        return self.current_scene_number

    def start(self):
        self.scenes[len(self.scenes) - 1].start()

    def handle_events(self, event, delta_time):
        self.scenes[len(self.scenes) - 1].handle_events(event, delta_time)

    def update(self, delta_time):
        self.scenes[len(self.scenes) - 1].update(delta_time)

    def render(self, window):
        self.scenes[len(self.scenes) - 1].render(window)

    def clear(self):
        self.scenes[len(self.scenes) - 1].clear()
