#!/usr/bin/env bash
set -euo pipefail

KEY_NAME="Cloche Signing Key"
KEY_EMAIL="packages@cloche.example"   #
SECRETS_REPO="cloche-project/packages" #

export GNUPGHOME=$(mktemp -d)
chmod 700 "$GNUPGHOME"
trap "rm -rf $GNUPGHOME" EXIT

cat > "$GNUPGHOME/keygen.batch" << EOF
%no-protection
Key-Type: RSA
Key-Length: 4096
Subkey-Type: RSA
Subkey-Length: 4096
Name-Real: $KEY_NAME
Name-Email: $KEY_EMAIL
Expire-Date: 2y
%commit
EOF

gpg --batch --gen-key "$GNUPGHOME/keygen.batch"

FINGERPRINT=$(gpg --list-secret-keys --with-colons | awk -F: '/^fpr/{print $10; exit}')
echo "Fingerprint: $FINGERPRINT"

read -rsp "Passphrase for key: " PASSPHRASE; echo

gpg --batch --pinentry-mode loopback \
    --passphrase "$PASSPHRASE" \
    --passwd "$FINGERPRINT" 2>/dev/null || true

PRIVATE_KEY_B64=$(gpg --armor --export-secret-keys "$FINGERPRINT" | base64 -w0)
PUBLIC_KEY_ARMOR=$(gpg --armor --export "$FINGERPRINT")

echo ""
echo "=== #) ==="
echo "$PUBLIC_KEY_ARMOR"
echo "======================================================"

if command -v gh &>/dev/null; then
  gh secret set GPG_PRIVATE_KEY --body "$PRIVATE_KEY_B64" --repo "$SECRETS_REPO"
  gh secret set GPG_PASSPHRASE  --body "$PASSPHRASE"      --repo "$SECRETS_REPO"
  echo "Secrets enviados."
else
  echo "gh CLI not found. Set manualy on Settings → Secrets:"
  echo "  GPG_PRIVATE_KEY = $PRIVATE_KEY_B64"
fi