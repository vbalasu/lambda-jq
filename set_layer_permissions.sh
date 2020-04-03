aws lambda add-layer-version-permission \
    --layer-name jq \
    --statement-id xaccount \
    --action lambda:GetLayerVersion  \
    --principal '*' \
    --version-number 1
