class PDController:
    # initialise the PD controller with specified gains
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp
        self.kd = kd
        # initial condition E[-1] = 0
        self.previous_error = 0

    # calculate the control action given the reference and observation
    def __call__(self, reference, observation):
        error = reference - observation

        #apply the PD control law to compute the control action
        control_action = (
            self.kp * error
            + self.kd * (error - self.previous_error)
        )

        # store the current error for the next iteration
        self.previous_error = error

        # return the computed control action to the closed loop simulation 
        return control_action