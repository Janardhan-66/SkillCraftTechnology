import re

def assess_password_strength(password):
    # Initialize score
    score = 0
    
    # Criteria 1: Length of password
    if len(password) >= 8:
        score += 2  # Strong length
    elif len(password) >= 6:
        score += 1  # Moderate length
    
    # Criteria 2: Presence of lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    
    # Criteria 3: Presence of uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    
    # Criteria 4: Presence of numbers
    if re.search(r'\d', password):
        score += 1
    
    # Criteria 5: Presence of special characters
    if re.search(r'[@$!%*?&#]', password):
        score += 2  # Special characters are highly valued
    
    # Strength assessment based on the score
    if score >= 7:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return score, strength

# Example usage
password = "Janardhan@2005"
score, strength = assess_password_strength(password)
print(f"Password: {password}\nScore: {score}\nStrength: {strength}")
