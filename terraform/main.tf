terraform {
  backend "gcs" {
    bucket = "debby-hand-knits-terraform"
    prefix = "/state/debby-hand-knits"
  }
}
