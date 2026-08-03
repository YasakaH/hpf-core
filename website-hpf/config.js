// HPF Research Workbench — client configuration.
// INTERNAL-ONLY SITE. This site must be protected at the edge with
// Cloudflare Access (see README.md). The login gate below is the in-app layer;
// Cloudflare Access is the authoritative boundary.
//
// users: username -> SHA-256 hex of the password.
// Generate hashes with: python scripts/hash_password.py <password>
// This is a convenience layer, not a security boundary.

window.HPF_CONFIG = {
  auth: {
    enabled: true,
    users: {
      "admin": "2b7f95d18895a0b2e4a88fd20a2ba78eca27f4da811ebaeec68152c57b067c89"
    }
  }
};
