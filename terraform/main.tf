terraform {
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 5.0"
        }
    }

    required_version = ">=0.14.9"

        backend "s3" {
            bucket = "[Remote_State_S3_Bucket_Name"
        }
}

provider "aws" {
    version = "~>5.0"
    region = var.aws_region
}
