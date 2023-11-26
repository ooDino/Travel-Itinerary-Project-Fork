terraform {
  backend "s3" {
    bucket = "terraform-state-nawayfarer-cs9490"
    key    = "core/terraform.tfstate"
    region = "us-east-1"
  }
}