# users = [
#     [1,'aouwal', 'Abdul Aouwal'],
#     [2,'samrat', 'Md. Samrat']
# ]
# print(users[0][1])

# user_id, user_name, user_full_name

wp_user = [{"id":1,"name":"Igor","url":"","description":"","link":"https:\/\/math.berkeley.edu\/wp\/blog\/author\/admin\/","slug":"admin","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=24&d=identicon&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=48&d=identicon&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/8d7a6e0f54977dbc6b6aa9f632f20ce3?s=96&d=identicon&r=g"},"meta":[],"_links":{"self":[{"href":"https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/users\/1"}],"collection":[{"href":"https:\/\/math.berkeley.edu\/wp\/wp-json\/wp\/v2\/users"}]}}]
# print(wp_user)
# print(len(wp_user))
# print(wp_user[0])
# print(type(wp_user[0]))
first_element = wp_user[0]
username = first_element.get('name')
slug = first_element.get('slug')
avatar = first_element.get('avatar_urls').get('96')
print(avatar)
# print(username, slug, sep="---")