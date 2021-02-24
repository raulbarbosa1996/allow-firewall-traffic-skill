from mycroft import MycroftSkill, intent_file_handler


class AllowFirewallTraffic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('traffic.firewall.allow.intent')
    def handle_traffic_firewall_allow(self, message):
        self.speak_dialog('traffic.firewall.allow')


def create_skill():
    return AllowFirewallTraffic()

