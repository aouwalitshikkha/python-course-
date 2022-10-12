heading = '  This is a        post title   '
slug = heading.strip()
while '  ' in slug:
    slug = slug.replace('  ',' ')

slug = slug.lower().replace(' ','-')
print(slug)