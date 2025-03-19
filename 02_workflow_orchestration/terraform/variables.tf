variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "sales-data-analysis-453808" #Your project ID here
}

variable "region" {
  description = "Project Region"
  default     = "europe-west3"
}

variable "location" {
  description = "Project Location"
  default     = "europe-west3"
}

variable "bq_datasets" {
  description = "My First BigQuery Datasets"
  default     = ["sales_data_analysis_dataset", "staging"]
}


variable "gcs_bucket_name" {
  description = "My Storage Bucket"
  default     = "sales_data_analysis_bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
