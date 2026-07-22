import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def sync_sheets_to_json():
    # 1. Autentikasi menggunakan file creds.json
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    client = gspread.authorize(creds)

    sheet_name = "SMART DASH 2026" # Ganti dengan nama file Google Sheets kamu
    try:
        sheet = client.open(sheet_name).sheet1
    except Exception as e:
        print(f"Gagal membuka spreadsheet: {e}")
        return

    # 3. Ambil seluruh data dalam bentuk list of dictionary
    data_records = sheet.get_all_records()

    # 4. Simpan ke file data.json agar bisa diakses oleh dashboard.html
    output_filename = "data.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(data_records, f, ensure_ascii=False, indent=4)
    
    print(f"Berhasil menyinkronkan {len(data_records)} baris data ke {output_filename}")

if __name__ == "__main__":
    sync_sheets_to_json()