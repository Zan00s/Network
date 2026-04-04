# Network
IP, ARP, ICMP, multicast, Static Routing, NTP, 

Проект по изучению базовых сетевых протоколов: IP, ARP, ICMP, multicast.Настройке и анализу прикладных и инфраструктурных протоколов.  
Среда: GNS3 + Wireshark.  

Задания и решения:

1.Расчет адресов >> ip-1

2.Развернута топология на базе Cisco 3745. (Настроены интерфейсы, проверена связность)

3.Multicast-запросы + анализ в Wireshark >> multicast.pcap + multicast.

4.ARP-запросы + анализ в Wireshark >> arp.pcap + arp.

5. Static Routing >> static.gns3project + static.pcap.
- Настроена цепочка `R1-R2-R3` с адресацией `/24`
- Реализована двусторонняя статическая маршрутизация
- Проверена связность через `ping`, проанализирован ICMP-трафик

6.NTP (Network Time Protocol) >> ntp.gns3project + ntp.pcap.
- Развернут NTP-сервер и клиент на соседних узлах
- Проведена синхронизация времени >> ntp.gns3project + ntp.pcap

7.DNS (Domain Name System) >> dns.gns3project + dns.pcap.
- Настроен DNS-сервер с записью для `my.site`
- Использован `loopback`-интерфейс для стабильной работы службы
- Проведён анализ DNS-запросов (Type, Class, порты)

8.DHCP (Dynamic Host Configuration Protocol) >> dhcp.gns3project + dhcp.pcap + dhcp.txt.
- Настроен DHCP-pool на 50 адресов (`10.10.30.0/24`)
- Зафиксирован процесс DORA (Discover, Offer, Request, Acknowledge)

9.SSH vs Telnet >> ssh.gns3project + ssh.pcap.
- Настроен безопасный удалённый доступ через SSH (RSA-ключи, VTY, локальный пользователь)
- Зафиксирован TCP 3-way handshake и сессия SSH
- Сравнительный анализ с открытым Telnet-трафиком

