variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "sales-data-analysis-453808"
}

variable "region" {
  description = "Project Region"
  default     = "europe-west3"
}

variable "location" {
  description = "Project Location"
  default     = "europe-west3"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "sales_data_analysis_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "sales_data_analysis_bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
