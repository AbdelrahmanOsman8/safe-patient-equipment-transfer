ِ# --------------------------------------------------------
# safe_patient_transfer.py
# Safe Patient & Equipment Transfer Simulation
# --------------------------------------------------------

# Initial Ward State
ward_a = ["Nurse", "Patient_1", "Patient_2", "Infusion_Pump"]
ward_b = []

# Rule Validation Function
def is_safe(side):
    # sourcery skip: assign-if-exp, boolean-if-exp-identity, reintroduce-else, remove-unnecessary-cast
    """Check if the side (ward) is safe"""
    if "Patient_1" in side and "Patient_2" in side and "Nurse" not in side:
        return False  # Patient_1 and Patient_2 cannot be left alone
    if "Patient_2" in side and "Infusion_Pump" in side and "Nurse" not in side:
        return False  # Infusion pump needs supervision with Patient_2
    return True

# Move Function
def move(item, source, destination):
    """Move an item from source to destination safely"""
    if item not in source:
        print(f"Cannot move {item}: Not in current ward!")
        return False

    source.remove(item)
    destination.append(item)

    if not is_safe(source) or not is_safe(destination):
        print(f"Unsafe move detected when moving {item}! Undoing move.")
        destination.remove(item)
        source.append(item)
        return False

    print(f"Moved {item} successfully!")
    return True

# Print current state
def print_state():
    print(f"Ward A: {ward_a}")
    print(f"Ward B: {ward_b}\n")


# --- Safe Transfer Sequence ---
print("Starting Safe Patient & Equipment Transfer Simulation...\n")

# Step 1: Nurse takes Patient_2 to Ward B
move("Nurse", ward_a, ward_b)
move("Patient_2", ward_a, ward_b)
print_state()

# Step 2: Nurse returns alone
move("Nurse", ward_b, ward_a)
print_state()

# Step 3: Nurse takes Patient_1 to Ward B
move("Nurse", ward_a, ward_b)
move("Patient_1", ward_a, ward_b)
print_state()

# Step 4: Nurse brings Patient_2 back to Ward A
move("Patient_2", ward_b, ward_a)
move("Nurse", ward_b, ward_a)
print_state()

# Step 5: Nurse takes Infusion_Pump to Ward B
move("Nurse", ward_a, ward_b)
move("Infusion_Pump", ward_a, ward_b)
print_state()

# Step 6: Nurse returns alone
move("Nurse", ward_b, ward_a)
print_state()

# Step 7: Nurse takes Patient_2 to Ward B
move("Nurse", ward_a, ward_b)
move("Patient_2", ward_a, ward_b)
print_state()

print("All patients and equipment transferred safely!")
