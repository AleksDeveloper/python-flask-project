terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }
}

provider "aws" {
  version = "~>5.0"
  region  = var.aws_region
}
