def get_certPreviewUrl(prev_fn, self, enrollment):
    """Cert preview URL comes from certificate info"""
    cert_info = self.get_cert_info(enrollment)
    return cert_info.get("download_url", None)
