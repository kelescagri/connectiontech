
İlk işlem olarak nginx klasöründe start.bat çift tıklanarak sunucu çalıştırılır.
pythonrequest.py scripti ile API den data çekilip overlay.txt içine yazılır.
convertToOverlayedVideo.py ile mp4 dosyası üzerine overlay.txt deki text eklenip yeni mp4 dosyası oluşturulur.
livestream.py scripti ile localhost da overlay yapılmış video yayınlanır.
livestream.py çalıştırıldıktan sonra yayın vlc playerde Ortam->Ağ Akışı Aç->Ağ altına rtmp://127.0.0.1/live/stream1 yazarak izlenebilir.
