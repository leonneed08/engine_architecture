# Bootstrap and service configuration
def configure_services():
    from services.locator import ServiceLocator
    from input.input_manager import InputManager
    ServiceLocator.register("input", InputManager())
