# 设计系统 (Design System)

## 概述

cloudQuant 设计系统确保产品界面的一致性、可访问性和开发效率。

### 设计原则

1. **数据优先**: 清晰展示数据，减少干扰
2. **专业可信**: 金融产品的严肃性和专业性
3. **高效操作**: 减少操作步骤，提供快捷方式
4. **响应迅速**: 即时反馈，流畅体验

### 设计价值观

| 价值观 | 描述 | 体现 |
|--------|------|------|
| **精准** | 金融数据需要精确 | 不四舍五入，显示完整精度 |
| **清晰** | 信息一目了然 | 良好的视觉层次 |
| **安全** | 风险始终可见 | 风险提示突出显示 |
| **高效** | 减少操作负担 | 快捷键、批量操作 |

## 设计令牌

### 颜色系统

#### 主色调

```text
品牌色:
├── Primary:    #2563EB (蓝色 - 信任、专业)
├── Secondary:  #10B981 (绿色 - 增长、盈利)
└── Accent:     #8B5CF6 (紫色 - 创新、AI)
```

#### 语义色

| 用途 | 颜色 | 说明 |
|------|------|------|
| Success | #10B981 | 盈利、成功、上涨 |
| Error | #EF4444 | 亏损、错误、下跌 |
| Warning | #F59E0B | 警告、注意 |
| Info | #3B82F6 | 信息、提示 |

#### 图表专用色

```css
/* K线图 */
--chart-bullish: #10B981;  /* 阳线 */
--chart-bearish: #EF4444;  /* 阴线 */

/* 多品种图表 */
--chart-color-1: #2563EB;
--chart-color-2: #10B981;
--chart-color-3: #F59E0B;
--chart-color-4: #8B5CF6;
--chart-color-5: #EC4899;
--chart-color-6: #06B6D4;
```

#### 中性色

```css
--gray-50:  #F9FAFB;
--gray-100: #F3F4F6;
--gray-200: #E5E7EB;
--gray-300: #D1D5DB;
--gray-400: #9CA3AF;
--gray-500: #6B7280;
--gray-600: #4B5563;
--gray-700: #374151;
--gray-800: #1F2937;
--gray-900: #111827;
```

### 排版

#### 字体族

```css
/* 主字体 */
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* 等宽字体 (代码、数字) */
--font-mono: 'JetBrains Mono', 'Fira Code', Consolas, monospace;

/* 中文字体 */
--font-chinese: 'PingFang SC', 'Microsoft YaHei', sans-serif;
```

#### 字号层级

| 层级 | 大小 | 行高 | 用途 |
|------|------|------|------|
| xs | 12px | 16px | 辅助信息、时间戳 |
| sm | 14px | 20px | 表格内容、标签 |
| base | 16px | 24px | 正文 |
| lg | 18px | 28px | 小标题 |
| xl | 20px | 28px | 卡片标题 |
| 2xl | 24px | 32px | 页面标题 |
| 3xl | 30px | 36px | 大标题 |
| 4xl | 36px | 40px | 数据展示 |

#### 字重

```css
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

### 间距

```css
--spacing-0: 0;
--spacing-1: 4px;
--spacing-2: 8px;
--spacing-3: 12px;
--spacing-4: 16px;
--spacing-5: 20px;
--spacing-6: 24px;
--spacing-8: 32px;
--spacing-10: 40px;
--spacing-12: 48px;
--spacing-16: 64px;
```

### 圆角

```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-full: 9999px;
```

### 阴影

```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1);
```

### 动效

```css
/* 时长 */
--duration-fast: 150ms;
--duration-normal: 300ms;
--duration-slow: 500ms;

/* 缓动函数 */
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

## 核心组件

### 按钮 (Button)

#### 变体

| 变体 | 用途 | 样式 |
|------|------|------|
| Primary | 主要操作 | 品牌色背景 |
| Secondary | 次要操作 | 边框样式 |
| Danger | 危险操作 | 红色背景 |
| Ghost | 轻量操作 | 无背景 |
| Link | 链接样式 | 下划线 |

#### 尺寸

| 尺寸 | 高度 | 内边距 |
|------|------|--------|
| sm | 32px | 8px 12px |
| md | 40px | 12px 16px |
| lg | 48px | 16px 24px |

#### 状态

- Default: 默认状态
- Hover: 悬停状态 (亮度 +10%)
- Active: 按下状态 (亮度 -10%)
- Focus: 聚焦状态 (外边框)
- Disabled: 禁用状态 (50% 透明度)

### 输入框 (Input)

#### 类型

- Text: 文本输入
- Number: 数字输入 (带步进按钮)
- Password: 密码输入
- Search: 搜索输入 (带搜索图标)
- Select: 下拉选择

#### 状态

- Default: 默认边框
- Focus: 蓝色边框 + 阴影
- Error: 红色边框 + 错误信息
- Disabled: 灰色背景 + 禁止输入

### 数据展示组件

#### 价格显示

```html
<!-- 上涨 -->
<span class="price price--up">+2.34%</span>

<!-- 下跌 -->
<span class="price price--down">-1.56%</span>

<!-- 不变 -->
<span class="price price--neutral">0.00%</span>
```

#### 数值显示

```html
<!-- 大数字 -->
<span class="number">
  <span class="number__value">1,234,567.89</span>
  <span class="number__unit">USDT</span>
</span>
```

### 卡片 (Card)

```text
┌─────────────────────────────────┐
│ Card Header                     │
├─────────────────────────────────┤
│                                 │
│ Card Content                    │
│                                 │
├─────────────────────────────────┤
│ Card Footer (optional)          │
└─────────────────────────────────┘
```

### 表格 (Table)

```html
<table class="table">
  <thead>
    <tr>
      <th>时间</th>
      <th>方向</th>
      <th class="text-right">数量</th>
      <th class="text-right">价格</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2026-03-13 10:30:00</td>
      <td><span class="badge badge--success">买入</span></td>
      <td class="text-right font-mono">0.1234</td>
      <td class="text-right font-mono">$42,567.89</td>
    </tr>
  </tbody>
</table>
```

## 布局模式

### 页面布局

```text
┌─────────────────────────────────────────────┐
│                  Header                      │
├──────────┬──────────────────────────────────┤
│          │                                  │
│  Sidebar │           Main Content           │
│          │                                  │
│          │                                  │
├──────────┴──────────────────────────────────┤
│                  Footer                      │
└─────────────────────────────────────────────┘
```

### 仪表板布局

```text
┌────────────┬────────────┬────────────┬────────────┐
│  指标卡片  │  指标卡片  │  指标卡片  │  指标卡片  │
├────────────┴────────────┴────────────┴────────────┤
│                                                   │
│                  主图表区域                        │
│                                                   │
├─────────────────────┬─────────────────────────────┤
│     交易列表        │        持仓信息              │
├─────────────────────┴─────────────────────────────┤
│                   风险指标                        │
└───────────────────────────────────────────────────┘
```

## 图表规范

### K线图

```typescript
interface CandlestickChart {
  // 数据
  data: Candle[];
  
  // 样式
  bullish: {
    color: '#10B981';
    borderColor: '#10B981';
  };
  bearish: {
    color: '#EF4444';
    borderColor: '#EF4444';
  };
  
  // 交互
  tooltip: boolean;
  crosshair: boolean;
  zoom: boolean;
}
```

### 收益曲线

```typescript
interface EquityCurve {
  data: { date: string; value: number }[];
  
  style: {
    lineColor: '#2563EB';
    lineWidth: 2;
    fillGradient: true;
  };
  
  markers: {
    maxDrawdown: true;
    peak: true;
  };
}
```

## 可访问性

### 色彩对比度

- 正文文字: 至少 4.5:1
- 大标题: 至少 3:1
- 交互元素: 至少 3:1

### 键盘导航

- Tab: 顺序导航
- Enter/Space: 激活
- Escape: 关闭/取消
- Arrow: 列表导航

### 屏幕阅读器

- 所有图片有 alt 文本
- 图表有描述性标题
- 数据表格有适当的 th/td 标记

## 响应式断点

```css
/* Mobile First */
--breakpoint-sm: 640px;   /* 手机 */
--breakpoint-md: 768px;   /* 平板 */
--breakpoint-lg: 1024px;  /* 小屏电脑 */
--breakpoint-xl: 1280px;  /* 桌面 */
--breakpoint-2xl: 1536px; /* 大屏 */
```

## 下一步

1. ✅ 完成设计系统 (本文档)
2. ⬜ 编写 PRD
3. ⬜ 测试计划
4. ⬜ 开始开发

---

*最后更新: 2026-03-13*
