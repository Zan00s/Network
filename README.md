# Network
IP, ARP, ICMP, multicast

 Проект по изучению базовых сетевых протоколов: IP, ARP, ICMP, multicast.  
 Среда: GNS3 + Wireshark.  

 Задания и решения:

Расчет адресов >> ip-1
Развернута топология на базе Cisco 3745. (Настроены интерфейсы, проверена связность)
Multicast-запросы + анализ в Wireshark >> multicast.pcap + multicast.
ARP-запросы + анализ в Wireshark >> arp.pcap + arp.


 Как запустить / воспроизвести

1. Установи [GNS3](https://www.gns3.com/) и импортируй образ Cisco IOS 3745.
2. Открой проект из папки `gns3/` (локально, не в репо).
3. Для анализа трафика используй встроенный Wireshark в GNS3 или экспортируй `.pcap`.
