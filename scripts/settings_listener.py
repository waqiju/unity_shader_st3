class SettingsListener(object):
    def __init__(self, settings):
        self.names = {}
        self.actions = {}
        self.settings = settings

    def add(self, name, action):
        self.names[name] = self.settings.get(name)
        self.actions[name] = action

    def onChanged(self):
        for name, value in self.names.items():
            settingsValue = self.settings.get(name)
            if value != settingsValue:
                self.actions[name]()
                self.names[name] = settingsValue
