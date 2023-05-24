output "data_bucket_id" {
  description = "S3 Bucket ID"
  value       = aws_s3_bucket.s3_module.id
}

