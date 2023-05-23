variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
  default     = "muhammad-hussam-bucket"
}

variable "region" {
  description = "AWS Region"
  default = "us-east-1"
}
