# TODO 쿠폰 발급. 2-d만 진행
# TODO CouponRule 가져온다
# TODO CouponTarget 가져온다.
from serverApi import server_api

# data = b'12345,56789'
data = b'38833'
# data = b'36483,36431'
decoded_data = data.decode('utf-8')
coupon_nos = [int(n) for n in decoded_data.split(',')]
print(coupon_nos)

server_api(
  "/coupons/issues",
  "POST",
  {
    "couponNos": coupon_nos,
    "memberIds": ["LRDZknKcL5gPtKCl1t1CF04MEx4ZP4OZBFKDsanvIgw="],
    "memberNos": [],
    "reason": ""
  }
)