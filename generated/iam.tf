# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam#google_project_iam_binding
resource "google_project_iam_binding" "my-custom-role-binding" {
  project = "my-project-id"
  role    = "roles/my-custom-role"
  members = [
        "user:john@mydomain.com",
        "user:jane@mydomain.com",
        "user:kim@mydomain.com",
  ]
}