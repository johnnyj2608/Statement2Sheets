# Statement2Sheets

Input: A PDF bank statement containing images of checks
Output: Extracted check images -> Extracted details from checks

Steps:
0. Train ML model to read handwriting
1. Extract Images from PDF
2. Preprocess image (grayscale, normalize)
3. Extract Text from image
4. POST details to Google Sheets

Dataset used: 
IAM Handwriting Database, data/lines.tgz + data/ascii.tgz