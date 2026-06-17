# Test settings dictionary
test_settings = {
    'theme': 'light',
    'language': 'english',
    'notifications': 'enabled'
}

# ── add_setting ──────────────────────────────────────────────────
def add_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

# ── update_setting ───────────────────────────────────────────────
def update_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# ── delete_setting ───────────────────────────────────────────────
def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'

# ── view_settings ────────────────────────────────────────────────
def view_settings(settings):
    if not settings:
        return 'No settings available.'
    result = 'Current User Settings:\n'
    for key, value in settings.items():
        result += f'{key.capitalize()}: {value}\n'
    return result

# Add a new setting
print(add_setting(test_settings, ('font_size', 'large')))

# Update an existing setting
print(update_setting(test_settings, ('theme', 'dark')))

# Delete a setting
print(delete_setting(test_settings, 'notifications'))

# View all settings
print(view_settings(test_settings))