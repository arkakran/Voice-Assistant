class HardwareController:
    def __init__(self, logger=None, simulate=True):
        self.simulate = simulate
        self.logger = logger
        self.devices = {
            "light": "PIN_17",
            "fan": "PIN_18"
        }

    def execute_action(self, device_name, action):
        if device_name not in self.devices:
            msg = f"Unknown device: {device_name}"
            print(msg)
            if self.logger:
                self.logger.log_hardware_event(msg)
            return

        pin = self.devices[device_name]

        if self.simulate:
            msg = f" [SIMULATION] {action.upper()} {device_name} (Pin: {pin})"
        else:
            # Add real GPIO/Arduino logic here
            msg = f" Executed {action.upper()} on {device_name} (Pin: {pin})"

        print(msg)
        if self.logger:
            self.logger.log_hardware_event(msg)
        return msg
