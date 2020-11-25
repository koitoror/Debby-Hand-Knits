terraform {
  backend "gcs" {
    bucket = "debby-hand-knits-terraform"
    prefix = "/state/storybooks"
  }
}
