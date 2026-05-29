# thread_0255: Re: [Internal]RE: Bluetooth-SIG認証 登録代行に関する御見積のお願い

- Message count: 1
- Source JSON: `thread_0255.json`

---

## 1. 2026-02-03 13:30

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu

後夷さんお疲れさまです。

HFP/HF/ACC/[ID]CとHFP/AG/SGSIT/SERR/[ID] はどちらもPTS

から bdAddr=0x00022E4E0025を指定したPaging接続を試みていますが、

どちらもPagingのSendから約41秒後に status=[ID] で

Page Timeoutによる「Failed to send BR/EDR ACL Connection Request.」

すなわちPaging接続に失敗しています。

DUTのPaging応答が正しければbdAddr=0x00022E4E0025が疑わしく、逆に

bdAddr=0x00022E4E0025が正しければDUTのPaging応答が疑われます。

また特定の対向相手からのPagingにしか対応しない実装の可能性があります。

<HFP/HF/ACC/[ID]>
