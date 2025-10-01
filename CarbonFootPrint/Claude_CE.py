from codecarbon import EmissionsTracker
import service

def get_llm_with_local_emissions(prompt):
    tracker = EmissionsTracker()
    tracker.start()
    try:
        output = service.get_CLAUDE_terraform_script(prompt)  
    finally:
        emissions_kg = tracker.stop()  # returns 
    return output, emissions_kg
