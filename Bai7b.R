install.packages("ineq")

library(ineq)

# Tỉ lệ tài sản của từng nhóm dân số
prop <- c(0, 0.2,0.2,0.2,0.2)

# Tính toán đường cong Lorenz và vẽ biểu đồ
lorenz_curve <- Lc(prop)
plot(lorenz_curve, xlab="Dân số", ylab="Của cải", main="Đường cong Lorenz thể hiện phân phối của cải với dân số")
