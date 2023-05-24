terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.20.0"
    }
  }
}

provider "aws" {
  
  region  = var.region
}

module "s3_module" {
  source      = "./s3_module"
  bucket_name = var.bucket_name
}

output "data_bucket_id" {
  value = module.s3_module.data_bucket_id
}

resource "aws_s3_object" "folder" {
  bucket = module.s3_module.data_bucket_id
  key    = "day2/IaC/"
  acl    = var.acl_value
  source = ""
}

