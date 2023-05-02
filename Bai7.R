# Cài đặt thư viện ineq
install.packages("ineq")
library(ineq)

# Tỉ lệ tài sản của từng nhóm dân số
# Vì phân phối đều nê ta phân 10% của cải thành 4 nhóm
prop <- c(0.8,0.025,0.025,0.025,0.025)

# Tính toán đường cong Lorenz và vẽ biểu đồ
lorenz_curve <- Lc(prop)
plot(lorenz_curve, xlab="Dân số", ylab="Của cải", main="Đường cong Lorenz thể hiện phân phối của cải với dân số")
