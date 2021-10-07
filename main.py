from jinja2 import Template
permissionsFile = open('permissions/my-custom-role.txt')
users = []
for user in permissionsFile.readlines():
    users.append(user.rstrip()) # remove whitespace/newline etc
    # TODO more validation
t = Template(open('template/project_iam_binding.j2').read())
generated = t.render(custom_role_name="my-custom-role", users=users, project_id="my-project-id")
f = open("generated/iam.tf", "w")
f.write(generated)
print(generated)
print("done")