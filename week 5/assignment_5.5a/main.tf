provider "aws" {
  region = "us-east-1"  # Change to your desired region
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = var.bucket_name
}

output "bucket_id" {
  value = aws_s3_bucket.example_bucket.id
}

