from wpilib import TimedRobot, Watchdog, run, XboxController, DigitalInput
from rev import CANSparkMax, CANSparkLowLevel


class Robot(TimedRobot):
    # Initialize Robot
    def robotInit(self):
        Watchdog(0.05, lambda: None).suppressTimeoutMessage(True)
        # the elevator on our robot has four motors. We must control all four to move it
        self.motor_l1 = CANSparkMax(26, CANSparkLowLevel.MotorType.kBrushed)
        self.motor_l2 = CANSparkMax(27, CANSparkLowLevel.MotorType.kBrushed)
        self.motor_r1 = CANSparkMax(24, CANSparkLowLevel.MotorType.kBrushed)
        self.motor_r2 = CANSparkMax(25, CANSparkLowLevel.MotorType.kBrushed)

        self.joystick = XboxController(0)

        self.top_limit_switch = DigitalInput(0)
        self.bottom_limit_switch = DigitalInput(1)

    def robotPeriodic(self) -> None:
        pass

    # Autonomous Robot Functions
    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def autonomousExit(self):
        pass

    # Teleop Robot Functions
    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # the same joystick value will be applied to each motor.
        # it is easier to store it in a variable than to call the function multiple times
        current_joystick_value = self.joystick.getLeftX()

        # this checks that if we are going up, the top limit switch is open (not pressed) and
        # if we are going down, make the opposie check
        if (current_joystick_value > 0 and not self.top_limit_switch.get()) or \
                (current_joystick_value < 0 and not self.bottom_limit_switch.get()):
            self.motor_l1.set(current_joystick_value)
            self.motor_l2.set(current_joystick_value)

            # the motors on the right side are opposite to the left motor, so need opposite power to be applied
            self.motor_r1.set(-current_joystick_value)
            self.motor_r2.set(-current_joystick_value)

    def teleopExit(self):
        # we do not want the motors to keep running if we transition between states
        self.motor_l1.set(0)
        self.motor_l2.set(0)
        self.motor_r1.set(0)
        self.motor_r2.set(0)

    # Test Robot Functions
    def testInit(self):
        pass

    def testPeriodic(self):
        pass

    def testExit(self):
        pass

    # Disabled Robot Functions
    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def disabledExit(self):
        pass

    def SimulationPeriodic(self) -> None:
        pass


# Start the Robot when Executing Code
if __name__ == "__main__":
    run(Robot)
