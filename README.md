# Network
IP, ARP, ICMP, multicast, Static Routing, NTP, DNS, DHCP, SSH,

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

10.VLAN & 802.1q Trunk >> task1.gns3.
- Развёрнута топология: 2 коммутатора (SW1, SW2) + 4 vPC
- Настроены VLAN 10 и 20, тегирование по стандарту 802.1q
- Реализовано Trunk-соединение между коммутаторами
- Проверена изоляция трафика: PC1 ↔ PC3 (VLAN 10), PC2 ↔ PC4 (VLAN 20)


11.EtherChannel (Link Aggregation) >> task2.gns3.
- На базе предыдущей топологии реализовано агрегирование каналов
- Использован протокол LACP (или PAgP) для объединения 2 физических линков в один логический
- Проверена отказоустойчивость: отключение одного линка не разрывает соединение

12. OSPF Dynamic Routing >> task3.gns.
- Построена топология из 3 маршрутизаторов (R1–R2–R3) с 4 подсетями
- Настроен OSPF в single-area (area 0)
- Проверена сквозная связность: ping между свободными интерфейсами R1 и R3
- Проанализирована таблица маршрутизации (`show ip route`)

13.HSRP Redundancy >> task4.gns.
- Развёрнута топология: 2 маршрутизатора + коммутатор + vPC в одной подсети
- Настроен HSRP с приоритетами: R1 — Active, R2 — Standby
- Проверено переключение при отказе активного шлюза
- Виртуальный IP используется как default gateway для клиента

14. SMB Traffic Analysis >> report.docx + report.pcap.
- Проанализирован дамп трафика в Wireshark
- Определена версия SMB-диалекта (SMBv1/v2/v3)
- Извлечены: Session ID, учётная запись, MAC-адреса сторон

15.Reverse Shell Detection >> answers.txt + some_troubled_traffic.pcapng.
- Исследован файл `some_troubled_traffic.pcapng`
- Выявлен reverse shell: источник, получатель, протокол
- Восстановлены переданные команды из потока данных

16. Packet Crafting with Scapy >> main.py + sent_message.pcapng.
- Написан Python-скрипт `main.py` для отправки TCP-пакета на `127.0.0.1:12345`
- Сообщение: `"Dear Steel Cat! This is no attack, it's my humster Pinkie you should track"`
- Перехвачен трафик в Wireshark, сохранён как `sent_message.pcapng`
- Добавлена валидация: скрипт проверяет, что дамп содержит ровно один пакет с нужной нагрузкой




