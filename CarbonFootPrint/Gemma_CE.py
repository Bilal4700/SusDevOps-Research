from codecarbon import EmissionsTracker
import service


def print_carbon_footprint(prompt):
        with EmissionsTracker() as tracker:
                service.get_GEMMA_terraform_script(prompt)

        print(f"\nCarbon emissions from computation: {tracker.final_emissions * 1000:.4f} g CO2eq")
        # print("\nDetailed emissions data:", tracker.final_emissions_data)
        
