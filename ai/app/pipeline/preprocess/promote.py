# flake8: noqa
PROMPT_TENDER_FILE_ANALYSIS = """
你是专业的招标文件分析专家。请从提供的招标文件中提取关键商务和技术条款，并严格按照以下JSON格式输出。
```json
{
  "tenderInfo": {
    "projectName": "项目全称",
    "bidderRequirements": "投标人资格要求",
    "keyTechnicalParameters": ["关键技术参数1", "关键技术参数2"],
    "paymentTerms": "付款条件",
    "warrantyPeriod": "质保期要求"
  }
}
```
只输出JSON，不要其他内容。
"""

PROMPT_FINAL_COMPARISON = """
你是专业的合同与招标文件对比分析专家。在接下来的用户消息中，你会收到一个包含`contractAnalysis`（合同分析结果）和`tenderAnalysis`（招标文件分析结果）的JSON对象。
请基于这份数据，进行全面、深入的对比分析，并严格按照下面指定的JSON格式输出最终的综合报告。

**输出JSON模板:**
```json
{
    "contract_id": "从输入数据中提取或生成一个唯一ID",
    "analysis_date": "生成当前日期和时间 (YYYY-MM-DD HH:MM:SS)",
    "templateType": "contract_with_tender",
    "projectInfo": {
        "projectName": "使用合同中的项目名称",
        "projectLocation": "使用合同中的项目地点",
        "projectArea": "提取或估算项目面积",
        "isProjectInfoConsistent": "对比项目名称、地点等信息后判断 (true/false)",
        "projectInfoDeviation": "如果不一致，在此详细说明偏差"
    },
    "parties": {
        "employer": "使用合同中的发包人名称",
        "contractorLead": "使用合同中的承包人牵头方",
        "contractorMember": "使用合同中的承包人成员方",
        "isPartiesConsistent": "对比发包人、承包人信息后判断 (true/false)",
        "partiesDeviation": "如果不一致，在此详细说明偏差"
    },
    "finance": {
        "contractPriceTotal": "使用合同中的总价 (数字)",
        "isPriceConsistent": "使用合同中的价格一致性判断 (true/false)",
        "priceInconsistencyDescription": "使用合同中的价格不一致描述"
    },
    "duration": {
        "totalDurationDays": "使用合同中的总工期 (数字)",
        "plannedStartDate": "使用合同中的计划开始日期",
        "plannedCompletionDate": "使用合同中的计划完成日期",
        "isDurationConsistent": "使用合同中的工期一致性判断 (true/false)",
        "durationInconsistencyDescription": "使用合同中的工期不一致描述"
    },
    "clauses": "直接从contractAnalysis中复制clauses对象",
    "assessment": "直接从contractAnalysis中复制assessment数组",
    "tenderCompliance": {
        "labels": ["项目基础信息符合性", "工期进度符合性", "质量标准符合性", "付款条件符合性", "担保保险符合性", "权责义务符合性", "风险责任符合性", "争议解决符合性"],
        "scores": "[根据对比分析，为每个label生成一个0-100的分数]"
    },
    "riskSummary": {
        "highRisk": "统计高风险项数量 (数字)",
        "mediumRisk": "统计中风险项数量 (数字)",
        "lowRisk": "统计低风险项数量 (数字)"
    },
    "complianceRate": "根据tenderCompliance的平均分计算整体符合率 (数字)",
    "priceDeviation": "详细描述合同总价与招标控制价的偏差率和分析",
    "durationDeviation": "详细描述合同工期与招标要求的差异及关键节点偏差",
    "technicalComparison": [
        {
            "category": "技术要求的类别，如'设计标准'",
            "tenderRequirement": "招标文件的具体要求",
            "contractClause": "合同中的对应条款",
            "compliance": "符合/偏离/轻微偏离",
            "riskLevel": "高/中/低"
        }
    ],
    "commercialComparison": [
        {
            "category": "商务条件的类别，如'付款条件'",
            "tenderRequirement": "招标文件的具体要求",
            "contractClause": "合同中的对应条款",
            "compliance": "符合/偏离",
            "impact": "该偏差对承包商的具体影响分析"
        }
    ],
    "managementComparison": [
        {
            "area": "管理领域，如'项目经理要求'",
            "tenderRequirement": "招标文件的具体要求",
            "contractClause": "合同中的对应条款",
            "consistency": "一致/不一致/基本一致"
        }
    ],
    "legalComparison": [
        {
            "clause": "法律条款，如'违约责任'",
            "tenderClause": "招标文件的具体条款",
            "contractClause": "合同中的对应条款",
            "difference": "详细说明两者差异"
        }
    ],
    "highRisks": [
        {
            "title": "高风险项的标题",
            "description": "详细描述风险内容",
            "impact": "该风险可能造成的影响",
            "timeline": "建议处理该风险的时间点",
            "category": "风险分类 (财务/管理/法律/技术)"
        }
    ],
    "mediumRisks": [
        {
            "title": "中风险项的标题",
            "description": "详细描述风险内容",
            "suggestion": "针对该风险的具体修改或应对建议",
            "category": "风险分类"
        }
    ],
    "lowRisks": [
        {
            "title": "低风险项的标题",
            "description": "详细描述风险内容",
            "category": "风险分类"
        }
    ],
    "immediateActions": [
        {
            "action": "需要立即执行的行动项",
            "description": "行动项的具体内容",
            "deadline": "完成时限 (如'签约前')",
            "responsible": "负责部门或团队"
        }
    ],
    "mediumTermSuggestions": [
        {
            "suggestion": "中期建议",
            "description": "建议的具体内容",
            "timeline": "建议执行的时间范围",
            "priority": "高/中/低"
        }
    ],
    "longTermOptimizations": [
        {
            "optimization": "长期优化建议",
            "description": "建议的具体内容",
            "expectedBenefit": "预期收益",
            "department": "负责部门"
        }
    ],
    "contractType": "从输入数据中提取合同类型"
}
```

**关键指令:**
1.  **数据来源**: 你的唯一信息来源是输入的`analysis_results_json`，它包含`contractAnalysis`和`tenderAnalysis`两部分。
2.  **结构严格**: 必须严格遵守上述JSON模板，不得增删或修改顶级字段。
3.  **内容填充**:
    - 对于明确指示为`直接从...复制`的字段，请直接复制对应的数据块。
    - 对于需要对比分析的字段（如`isProjectInfoConsistent`, `technicalComparison`等），请基于输入数据进行逻辑判断和信息提取。
    - 对于需要生成的字段（如`analysis_date`, `scores`, `complianceRate`等），请根据指令进行计算或生成。
4.  **数值格式**: 所有表示金额、数量、天数、百分比、得分的字段，其值必须是**数字(Number)**，而不是字符串。
5.  **空值处理**: 如果某个字段在源数据中找不到对应内容，请使用合理的默认值（例如，字符串用`""`，数组用`[]`，对象用`{}`）。

现在，请开始分析并生成最终的综合报告。
"""


#合同类别分析
PROMPT_INITIAL_ANALYSIS = """
你是一个专业的工程合同分析专家，精通建筑工程EPC总承包合同、施工合同等各类工程合同的条款解析、风险识别和差异对比分析。你具备深厚的工程管理、造价控制、法律法规和合同管理专业知识。
请根据合同的标题和开头部分内容，快速判断合同类型并提取最核心的项目信息。
标准合同范本库
必须从以下标准范本中识别合同类型：
1. 《建设项目工程总承包合同（示范文本）》（GF-2020-0216）
2. 《浙江省房屋建筑和市政基础设施建设工程文件示范文本（2024版）》
3. 《建设工程监理合同（示范文本）》（GF-2012-0202）
4. 《建设工程设计合同示范文本（房屋建筑工程）》（GF-2015-0209）
5. 《建设工程勘察合同（示范文本）》（GF-2016-0203）
6. 《建设工程施工合同（示范文本）》（GF-2017-0201）
7. 《浙江省房屋建筑和市政基础设施建设工程监理的合同示范文本（2024版）》

合同类型识别规则
根据以下特征判断合同类型：
• EPC总承包合同：包含设计、采购、施工全过程承包内容 → 适用GF-2020-0216或浙江省2024版EPC范本
• 施工承包合同：仅包含施工内容，无设计采购 → 适用GF-2017-0201或GF-2020-2605
• 监理合同：监理服务相关内容 → 适用GF-2012-0202或浙江省2024版监理范本
• 设计(房屋建筑工程)合同：设计服务相关内容 → 适用GF-2015-0209
• 勘察合同：勘察服务相关内容 → 适用GF-2016-0203
请根据合同的标题和开头部分内容，快速判断合同类型并提取最核心的项目信息。
**输出要求:**
- 只输出JSON格式。
- JSON中必须包含 `contractType` 和 `projectInfo` 字段。
- `contractType` 的值必须从这里面选择: "epc", "施工", "监理", "设计_房屋建筑工程", “勘察”,"generic"。

**示例:**
```json
{
  "contractType": "epc",
  "projectInfo": {
    "projectName": "项目全称（如果能快速找到）"
  }
}
```
请开始分析以下合同内容：
"""

PROMPT_PART_1_REFINED = """
你是专业的合同分析专家。请从"第一部分 合同协议书"中提取基础信息，特别注意合同编号、金额和时间的准确性检查。

**合同编号**：确保合同编号格式正确且一致，如果缺失，需指出。

**金额检查重点：**
1. 合同总价是否等于各分项费用之和
2. 分项费用之和是否等于合同总价  
3. 数字与大写金额是否一致
4. 是否存在计算错误或遗漏项
5. **识别空白/未填写字段**：
   - 税率是否填写（如"__  /  __"或"__    __"表示未填）
   - 税金是否填写
   - 暂估价是否填写
   - 其他费用项是否填写

**时间检查重点：**
1. 按起止日期计算的实际天数是否与总工期一致
2. 工期单位是否统一（日历天/工作日）
3. 里程碑时间安排是否合理
4. 是否存在时间逻辑错误

**检查方法：**
- 金额：将所有分项费用相加，与合同总价对比
- 时间：用结束日期减去开始日期，与总工期对比
```json
{
  "projectInfo": {
    "projectName": "项目全称",
    "projectLocation": "项目地点",
    "projectFundingSource": "项目资金来源",
    "page": "页码"
  },
  "parties": {
    "employer": "发包人名称",
    "contractorLead": "承包人（牵头方）",
    "contractorMember": "承包人（成员方）",
    "page": "页码"
  },
  "finance": {
    "contractPriceTotal": "合同总价数值",
    "contractPriceTotalChinese": "合同总价大写",
    "page": "页码",
    "isPriceConsistent": "true/false",
    "priceInconsistencyDescription": "仅在isPriceConsistent为false时填写，如果合同总价X元与分项合计Y元不符，则必须写明：合同总价X元与分项合计Y元不符，差额Z元，如相符，则写合同总价X元与分项合计Y元相符"；XX项未填写；
    "components": [
      {"name": "识别出的费用项名称1", "value": "金额数值1", "chinese": "大写金额1"},
      {"name": "识别出的费用项名称2", "value": "金额数值2", "chinese": "大写金额2"}
    ]
  },
  "duration": {
    "totalDurationDays": "总工期天数",
    "plannedStartDate": "YYYY-MM-DD",
    "plannedCompletionDate": "YYYY-MM-DD",
    "page": "页码",
    "isDurationConsistent": "true/false",
    "durationInconsistencyDescription": "仅在isDurationConsistent为false时填写， 必须写明：按起止日期计算实际工期X天，与约定的Y天不符，相差Z天；如果表述上出现“日历天”和“天”这种不一致,也应该写出来",
    "projectMilestones": [
      {
        "name": "里程碑名称",
        "timePoint": "时间点描述",
        "description": "里程碑具体描述"
      }
    ]
  },
  "qualityStandards": {
    "designQuality": "设计质量标准",
    "constructionQuality": "施工质量标准",
    "excellenceTarget": "工程创优目标",
    "page": "页码"
  }
}
```
**重要提醒：**
1. 必须进行实际计算验证，不能凭感觉判断
2. 如果发现不一致，description字段必须包含具体数值
3. 所有page字段必须是数字，不加引号
4. 所有金额和工期必须是数值，不加引号

只输出JSON，不要其他内容。
"""



# ============================================================
# 文件说明：第一部分合同协议书二级拆分实现
# 需要添加到现有的合同分析代码中
# ============================================================


PROMPT_PART1_项目与当事人 = """
你是专业的合同信息提取专家。请从提供的文本中提取项目基础信息和参与方信息。

**提取内容：**
1. 项目名称、地点、资金来源
2. 工程批准文号、投资金额
3. 工程内容和规模
4. 发包人、承包人（含联合体成员）
5. 项目经理姓名

**输出JSON格式：**
```json
{
  "projectInfo": {
    "projectName": "完整项目名称",
    "projectLocation": "详细地址",
    "projectFundingSource": "资金来源说明",
    "approvalNumber": "批准文号",
    "investmentAmount": "投资估算金额（数值）+单位（万元\元）",
    "budgetAmount": "工程概算金额（数值）+单位（万元\元）",
    "constructionCost": "建安工程造价（数值）+单位（万元\元）",
    "projectScale": "工程规模描述（用地面积、建筑面积等）"
  },
  "parties": {
    "employer": "发包人全称",
    "contractorLead": "承包人牵头方全称",
    "contractorMembers": ["成员方1", "成员方2"]
  },
  "projectManager": {
    "name": "项目经理姓名"
  }
}
```

**注意事项：**
- 所有金额必须是纯数字+含单位
- 如果某项信息未找到，填写 null
- projectScale 尽量包含完整的面积信息

只输出JSON，不要任何解释。
"""

PROMPT_PART1_设计合同_项目与当事人 = """
你是专业的设计合同信息提取专家。请从提供的文本中提取项目基础信息和参与方信息。

**设计合同特点：**
- 通常有三方：发包人、代建方（如果有）、设计人
- 金额通常是"建安造价估算"或"投资估算"
- 项目负责人包括：发包人代表、设计人项目负责人

**提取内容：**
1. 项目名称、地点
2. 投资估算、建安造价（注意区分）
3. 工程规模（用地面积、建筑面积、容积率等）
4. 发包人（含发包人代表）、设计人（主设计单位）、代建方
5. 设计人项目负责人姓名

**字段映射规则（重要）：**
- `employer` → 发包人全称，如果有发包人代表，在后面加括号："发包人全称（代表：姓名）"；如果没有发包人代表，只填发包人全称
- `contractorLead` → 设计人全称（主设计单位）
- `contractorMembers` → 如果有代建方，填入数组；如果有联合体成员方，也填入数组
- `projectManager.name` → 设计人项目负责人姓名

**金额识别规则（重要）：**
- "投资估算：XX亿元" → `investmentAmount`
- "工程概算：XX万元" → `budgetAmount`
- "建安造价：XX亿元" → `constructionCost`
- 如果只有"投资估算：建安造价约5亿元"，这种情况建安造价填入 `constructionCost`

**金额格式要求：**
- 统一转换为"万元"单位
- 格式：纯数字 + "万元"
- 例如：
  - "5亿元" → `50000` + "万元"
  - "500万元" → `500` + "万元"
  - "约5亿元" → `50000` + "万元"（去掉"约"）

**输出JSON格式：**
```json
{
  "projectInfo": {
    "projectName": "完整项目名称",
    "projectLocation": "详细地址",
    "projectFundingSource": null,
    "approvalNumber": null,
    "investmentAmount": null或"数字+万元",
    "budgetAmount": null或"数字+万元",
    "constructionCost": "数字+万元",
    "projectScale": "规划用地XX平方米，地上建筑面积XX平方米，地下建筑面积XX平方米"
  },
  "parties": {
    "employer": "发包人全称"或"发包人全称（代表：姓名）",
    "contractorLead": "设计人全称",
    "contractorMembers": ["代建方全称"]或[]
  },
  "projectManager": {
    "name": "设计人项目负责人姓名"或null
  }
}
```

**示例：**

**输入文本：**
```
发包人：杭州市滨江区区级机关事务管理服务中心
发包人代表：徐俊
代建方：杭州滨江城建发展有限公司
设计人：浙江华坤建筑设计院有限公司
工程名称：滨江区公安、交警、消防业务用房项目设计(重新招标)
工程地点：杭州市滨江区西兴北控规单元内
规划用地20148平方米，地上建筑面积约64000平方米，地下建筑面积约26000平方米
投资估算：建安造价约5亿元
设计人项目负责人：张三
```

**输出：**
```json
{
  "projectInfo": {
    "projectName": "滨江区公安、交警、消防业务用房项目设计(重新招标)",
    "projectLocation": "杭州市滨江区西兴北控规单元内",
    "projectFundingSource": null,
    "approvalNumber": null,
    "investmentAmount": null,
    "budgetAmount": null,
    "constructionCost": "50000万元",
    "projectScale": "规划用地20148平方米，地上建筑面积约64000平方米（其中公安分局指挥中心业务用房约28774平方米，交警大队业务用房约14000平方米，消防大队业务用房约16067平方米），地下建筑面积约26000平方米"
  },
  "parties": {
    "employer": "杭州市滨江区区级机关事务管理服务中心（代表：徐俊）",
    "contractorLead": "浙江华坤建筑设计院有限公司",
    "contractorMembers": ["杭州滨江城建发展有限公司"]
  },
  "projectManager": {
    "name": "张三"
  }
}
```

**注意事项：**
- 所有金额统一为"万元"单位的纯数字
- 如果某项信息未找到，填写 null
- projectScale 尽量包含完整的面积、容积率等信息
- 代建方放入 contractorMembers 数组
- 如果有发包人代表，在employer字段后加括号："发包人全称（代表：姓名）"；如果没有发包人代表，只填发包人全称
- projectManager.name 只填设计人项目负责人
- 如果没有代建方，contractorMembers 为空数组 []

只输出JSON，不要任何解释。
"""

PROMPT_PART1_监理合同_项目与当事人 = """
你是专业的监理合同信息提取专家。请从提供的文本中提取项目基础信息和参与方信息。

**监理合同特点：**
- 通常有两方：委托人（发包人）、监理人（承包人）
- 金额通常是"工程概算"（用于计算监理费）
- 项目负责人是"总监理工程师"（可能包含身份证号、注册号）

**提取内容：**
1. 工程名称、地点
2. 工程概算金额（注意：这是被监理工程的概算，不是监理费）
3. 工程规模（建筑面积、层数、高度等）
4. 委托人、监理人
5. 总监理工程师姓名（及身份证号、注册号）

**字段映射规则（重要）：**
- `employer` → 委托人全称
- `contractorLead` → 监理人全称
- `contractorMembers` → 如果有联合体成员，填入数组；通常为空数组[]
- `projectManager.name` → 总监理工程师姓名
- `budgetAmount` → 工程概算金额（这是被监理工程的概算）
- `investmentAmount` → 通常为null（监理合同一般不涉及总投资）
- `constructionCost` → 通常为null（监理合同一般不单独列建安造价）

**金额格式要求：**
- 统一转换为"万元"单位
- 格式：纯数字 + "万元"
- 例如：
  - "工程概算104645万元" → `104645` + "万元"
  - "工程概算10.46亿元" → `104600` + "万元"

**输出JSON格式：**
```json
{
  "projectInfo": {
    "projectName": "完整工程名称",
    "projectLocation": "详细地址",
    "projectFundingSource": null,
    "approvalNumber": null,
    "investmentAmount": null,
    "budgetAmount": "数字+万元",
    "constructionCost": null,
    "projectScale": "总建筑面积XX平方米，最高XX层，地下XX层，建筑高度XX米"
  },
  "parties": {
    "employer": "委托人全称",
    "contractorLead": "监理人全称",
    "contractorMembers": []
  },
  "projectManager": {
    "name": "总监理工程师姓名"
  }
}


**注意事项：**
- 所有金额统一为"万元"单位的纯数字
- 如果某项信息未找到，填写 null
- projectScale 尽量包含完整的面积、层数、高度信息，如果有分项（如公共租赁房、共有产权房），也要包含
- 监理合同通常只有budgetAmount（工程概算），investmentAmount和constructionCost通常为null
- projectManager.name 只填总监理工程师姓名，不包含身份证号和注册号
- contractorMembers 通常为空数组[]（监理合同一般不涉及联合体）

只输出JSON，不要任何解释。
"""

PROMPT_PART1_承包范围 = """
你是专业的合同范围分析专家。请从"工程承包范围"章节中提取四大类工作内容。

**提取目标：**
1. 设计工作内容（包括哪些专业设计）
2. 采购工作内容（设备材料采购）
3. 施工工作内容（包括哪些工程）
4. 总承包管理及服务内容

**输出JSON格式：**
```json
{
  "contractScope": {
    "design": "设计工作的详细描述，包括专业类型",
    "procurement": "采购工作的详细描述",
    "construction": "施工工作的详细描述",
    "management": "总承包管理和服务工作的详细描述"
  }
}
```

**提取原则：**
- 保持原文的关键信息，适当精简
- 每项不超过200字
- 如果某项未明确说明，填写"未明确约定"

只输出JSON，不要任何解释。
"""

PROMPT_PART1_承包范围_勘察 = """
你是专业的勘察合同分析专家。请从"勘察范围和阶段、技术要求及工作量"章节中提取四大类工作内容。

**提取目标及字段映射：**
1. design - 勘察范围：勘察的地理范围、项目范围、涉及的地块或区域
2. procurement - 勘察阶段与方案：勘察阶段划分（初勘/详勘等）、方案依据、基础资料要求
3. construction - 技术要求与工作量：适用的规范标准、编制深度要求、勘探点/钻孔/取样等具体工作量
4. management - 成果交付与配合：需提交的报告资料、参会要求、验收配合等服务内容

**输出JSON格式：**
```json
{
  "contractScope": {
    "design": "勘察范围的详细描述，包括项目地块、勘察区域等",
    "procurement": "勘察阶段与方案的详细描述，包括阶段划分、方案依据等",
    "construction": "技术要求与工作量的详细描述，包括适用规范、具体工作量等",
    "management": "成果交付与配合工作的详细描述，包括报告提交、会议配合、验收配合等"
  }
}
```

**提取原则：**
- 保持原文的关键信息，适当精简
- 同一条款内容可能涉及多个字段，需拆分归类到对应字段
- 每项不超过200字
- 如果某项未明确说明，填写"未明确约定"

只输出JSON，不要任何解释。
"""

PROMPT_PART1_承包范围_设计 = """
你是专业的设计合同分析专家。请从"工程设计范围、阶段与服务内容"章节中提取四大类工作内容。

**设计合同字段映射规则（重要）：**
1. design → 设计专业内容：提取具体包含哪些专业（建筑、结构、给排水、暖通、电气、弱电、幕墙、装修、景观、市政等）
2. procurement → 设计范围：提取设计范围和类型（方案设计、初步设计、施工图设计、BIM设计、交评、能评、环评、日照分析等评估类项目）
3. construction → 技术标准要求：提取技术要求、深度要求、成果标准（如符合国家图纸编制深度规定、审查要求、完整性准确性要求等）
4. management → 设计服务内容：提取全过程服务内容（图纸会审、技术交底、施工指导、设计变更、材料设备技术要求、验收配合、后续服务等）

**提取原则：**
- 从原文中归纳总结，不要逐字照抄
- 每个字段提取核心要点，保持简洁
- 每项不超过200字
- 如果某项未明确说明，填写"未明确约定"

**输出JSON格式：**
```json
{
  "contractScope": {
    "design": "设计专业内容的描述",
    "procurement": "设计范围的描述",
    "construction": "技术标准要求的描述",
    "management": "设计服务内容的描述"
  }
}
```

**注意事项：**
- design字段：聚焦"设计专业"（建筑、结构、机电等）
- procurement字段：聚焦"设计范围"（方案、初设、施工图、评估类等）
- construction字段：聚焦"技术标准"（深度要求、审查要求、成果标准等）
- management字段：聚焦"服务内容"（会审、交底、指导、变更、验收等）
- 每个字段简洁概括，不超过200字

只输出JSON，不要任何解释。
"""



PROMPT_PART1_工期验算 = """
你是专业的合同工期审计专家。请从"合同日期"章节中提取工期信息并进行验算。

**日期提取规则：**
- 如果日期完整（如2021-09-15），直接提取
- 如果日期不完整（如2021年09月  日），提取为 "2021-09-XX" 并在 description 中说明
- plannedStartDate 和 plannedCompletionDate 都必须按此规则处理

**必须完成的验算：**
1. 提取计划开始日期和计划竣工日期
2. 计算实际天数 = 竣工日期 - 开始日期
3. 对比约定的总工期天数
4. 检查单位一致性（日历天 vs 工作日）
5. 提取所有里程碑节点

**输出JSON格式：**
```json
{
  "duration": {
    "totalDurationDays": 总工期数值+"日历天"或者"天"(需要根据原文判断),
    "plannedStartDate": "YYYY-MM-DD",   #若无DD，则写（具体日期未填写）
    "plannedCompletionDate": "YYYY-MM-DD",
    "calculatedDays": 计算出的实际天数(数值)+"日历天"或者"天"(需要根据原文判断),
    "isDurationConsistent": true/false,
    "durationInconsistencyDescription": "仅在不一致时填写：按起止日期计算X天，与约定Y天不符，相差Z天；或说明单位不一致问题",
    "projectMilestones": [
      {
        "name": "里程碑名称（如：桩基完成）",
        "timePoint": "时间点描述（如：开工后100天）",
        "deadline": "具体日期（如果能计算出来）",
        "description": "具体要求描述"
      }
    ]
  }
}
```

**验算要求：**
- 必须实际计算天数，不能凭感觉
- 总工期数值和计算的天数后面必须注明单位："日历天"或者"天"(需要根据原文判断)
- 日期格式不完整时（如只有年月），在description中说明
- 所有天数必须是数值类型

只输出JSON，不要任何解释。
"""

# ============================================================
# 工期验算三步式拆分（适配小模型）
# ============================================================

PROMPT_PART1_工期验算_STEP1_基础信息提取 = """
你是专业的合同信息提取专家。请从"合同日期"章节中提取基础工期信息。

**重要：只提取信息，不做任何计算和验证！**

**提取任务：**
1. 提取计划开始日期（原文是什么就提取什么）
2. 提取计划竣工日期（原文是什么就提取什么）
3. 提取工期总日历天数（原文是什么就提取什么）
4. 识别工期单位（日历天/工作日/天）

**日期处理规则：**
- 如果日期完整（如2021-09-15），直接提取为 "2021-09-15"
- 如果日期不完整（如2021年09月  日），提取为 "2021-09-XX"
- 如果年份不完整（如  年  月  日），提取为 "未填写"

**输出JSON格式：**
```json
{
  "totalDurationDays": "790 日历天",
  "plannedStartDate": "2021-09-XX",
  "plannedCompletionDate": "2021-XX-XX",
  "unit": "日历天",
  "startDateComplete": false,
  "completionDateComplete": false,
  "durationUnit": "日历天"
}
```

**字段说明：**
- `totalDurationDays`: 原文中的工期总天数（保留单位，如"790 日历天"）
- `plannedStartDate`: 计划开始日期（YYYY-MM-DD或YYYY-MM-XX格式）
- `plannedCompletionDate`: 计划竣工日期（YYYY-MM-DD或YYYY-MM-XX格式）
- `unit`: 从原文中识别的工期单位
- `startDateComplete`: 开始日期是否完整填写（true/false）
- `completionDateComplete`: 竣工日期是否完整填写（true/false）
- `durationUnit`: 工期单位（日历天/工作日/天）

**重要提醒：**
- 不要进行天数计算
- 不要进行一致性验证
- 不要提取里程碑信息
- 只输出JSON，不要任何解释

只输出JSON，不要任何解释。
"""

PROMPT_PART1_工期验算_STEP2_里程碑提取 = """
你是专业的合同信息提取专家。请从"合同日期"章节中提取所有工期里程碑信息。

**重要：只提取里程碑信息，不做任何计算！**

**提取任务：**
1. 识别所有工期节点和里程碑
2. 提取每个里程碑的名称
3. 提取每个里程碑的时间点描述（原文描述）
4. 提取每个里程碑的具体要求

**输出JSON格式：**
```json
{
  "projectMilestones": [
    {
      "name": "投标阶段完成桩基及围护施工图设计",
      "timePoint": "投标阶段",
      "description": "投标阶段完成桩基及围护施工图设计"
    },
    {
      "name": "中标通知书后55日历天内完成施工图设计文件",
      "timePoint": "中标通知书后55日历天",
      "description": "完成结构、建筑、水电、暖通、消防的施工图设计文件及相关图审、报批等工作"
    },
    {
      "name": "完成全部桩基工程施工",
      "timePoint": "开工令后100日历天",
      "description": "监理签发的"开工令"之日后100日历天内完成全部桩基工程施工"
    }
  ]
}
```

**字段说明：**
- `name`: 里程碑简短名称
- `timePoint`: 时间点描述（直接从原文提取，如"开工令后100日历天"）
- `description`: 里程碑的完整描述

**提取原则：**
- 尽可能提取所有里程碑
- 保持原文的时间点描述
- description应该完整且准确
- 不要计算具体日期

**重要提醒：**
- 不要计算deadline
- 不要进行验算
- 只输出JSON，不要任何解释

只输出JSON，不要任何解释。
"""

PROMPT_PART1_工期验算_STEP3_工期验算 = """
你是专业的工期验算专家。现在需要基于已提取的基础信息和里程碑信息进行工期验算。

**输入数据：**
基础信息：{basic_info}
里程碑信息：{milestones}

**验算任务：**
1. 如果起止日期完整，计算实际天数
2. 对比计算天数与约定总工期
3. 检查工期单位一致性
4. 为每个里程碑计算具体截止日期（如果可以）

**计算规则：**
- 只有当开始日期和竣工日期都完整时，才计算天数
- 日期计算使用日历天
- 如果日期不完整，calculatedDays设为"无法计算（日期不完整）"
- 里程碑deadline计算：如果开始日期完整，则计算；否则设为null

**一致性判断：**
isDurationConsistent 为 true 需同时满足：
1. 起止日期都完整
2. 计算天数 = 约定总工期（允许±1天误差）
3. 工期单位一致（都是"日历天"或都是"天"）

否则为 false

**输出JSON格式：**
```json
{
  "duration": {
    "totalDurationDays": "790 日历天",
    "plannedStartDate": "2021-09-XX",
    "plannedCompletionDate": "2021-XX-XX",
    "calculatedDays": "无法计算（日期不完整）",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": [
      {
        "name": "完成全部桩基工程施工",
        "timePoint": "开工令后100日历天",
        "deadline": null,
        "description": "监理签发的"开工令"之日后100日历天内完成全部桩基工程施工"
      }
    ]
  }
}
```

**durationInconsistencyDescription格式：**
如果不一致，描述格式：
- 日期不完整："计划开始日期不完整（2021-09-XX），计划竣工日期不完整（2021-XX-XX），无法验算工期"
- 天数不符："按起止日期计算X天，与约定Y天不符，相差Z天"
- 单位不一致："总工期使用'日历天'，但计算天数使用'天'，单位不一致"

如果一致，为空字符串 ""

**重要提醒：**
- 日期不完整时，不要强行计算
- deadline为null是正常的（当日期不完整时）
- 必须输出完整的duration对象，包含所有字段
- 只输出JSON，不要任何解释

只输出JSON，不要任何解释。
"""



PROMPT_PART1_金额验算 = """
你是专业的合同造价审计专家。请从"签约合同价"章节中提取价格信息并进行严格验算。

**重要：JSON格式铁律**
绝对禁止：calculatedSum字段中出现加法表达式（如：1000 + 2000 + 3000）
必须执行：先在草稿纸上计算总和，然后只填写最终数字结果

**提取任务：**
1. 提取合同总价（数字和大写）
2. 提取所有分项费用及其税率、税金
3. 在心里或草稿上计算：已填写分项的value总和
4. 将计算结果（一个纯数字）填入calculatedSum

**严格验证规则：**
只有同时满足以下所有条件，isPriceConsistent才为true：
- 所有分项value都是数值（无"未填写"）
- 所有分项taxRate都已填写（无"未填写"）
- 所有分项tax都已填写（无"未填写"）  
- 分项value总和 = contractPriceTotal
- 数字与大写金额一致

否则isPriceConsistent = false

**priceInconsistencyDescription要求：**
列出所有问题，格式：
"XXX金额未填写; XXX税率未填写; XXX税率已填写但税金未填写; 合同总价X元与分项合计Y元不符，差额Z元"
无问题则为空字符串""

**输出要求：**
第一步：在脑海中完成计算
- 假设分项value为：27993900, 3772285700, 269395100, 12505400, 74619000
- 暂估价为"未填写"，跳过不计算
- 在心里算出总和 = 4156799100

第二步：将计算结果填入JSON
- calculatedSum: 4156799100（这是计算好的数字，不是算式！）

第三步：输出纯JSON
- 不要```json```标记
- 不要任何解释文字
- calculatedSum必须是一个纯数字

**JSON结构模板：**
{
  "finance": {
    "contractPriceTotal": 数字,
    "contractPriceTotalChinese": "大写",
    "calculatedSum": 数字（不是算式！直接写计算结果！）,
    "isPriceConsistent": true或false,
    "priceInconsistencyDescription": "问题描述或空字符串",
    "priceFormType": "价格形式",
    "components": [
      {
        "name": "项目名",
        "value": 数字或"未填写",
        "chinese": "大写或未填写",
        "taxRate": "百分比或未填写",
        "tax": 数字或"未填写"
      }
    ]
  }
}

**错误示例（绝对禁止）：**
"calculatedSum": 27993900 + 3772285700 + 12505400  

**正确示例：**
"calculatedSum": 4156799100  

请立即提取并输出JSON，calculatedSum必须是计算好的数字！

"""

# ============================================================
# 第一步：信息提取（不做计算）
# ============================================================
PROMPT_PART1_金额验算_STEP1_提取价格信息 = """
你是专业的合同信息提取专家。请从"签约合同价"章节中提取所有价格相关信息。

**任务要求：**
1. 提取合同总价（数字和大写）
2. 提取所有分项费用的名称、金额、大写、税率、税金
3. 只提取信息，不进行任何计算和验证

**重要：**
- 如果某个字段在合同中未出现，填写"未填写"
- 不要尝试计算或推断任何数值
- 不要进行一致性验证

**输出格式：**
纯JSON，不要```json```标记，不要任何解释文字

**JSON结构：**
{
  "contractPriceTotal": 数字或null,
  "contractPriceTotalChinese": "大写或未填写",
  "priceFormType": "价格形式或未填写",
  "components": [
    {
      "name": "分项名称",
      "value": 数字或null,
      "chinese": "大写或未填写",
      "taxRate": "百分比或未填写",
      "tax": 数字或null
    }
  ]
}

**示例：**
{
  "contractPriceTotal": 4156799100,
  "contractPriceTotalChinese": "人民币(大写)肆拾壹亿伍仟陆佰柦拾玖万玖仟壹佰元整",
  "priceFormType": "总价合同",
  "components": [
    {
      "name": "设计费(含税)",
      "value": 27993900,
      "chinese": "人民币(大写)贰仟柒佰玖拾玖万叁仟玖佰元整",
      "taxRate": "6%",
      "tax": 1584560
    },
    {
      "name": "建筑安装工程费(含设备购置费)(含税)",
      "value": 3772285700,
      "chinese": "人民币(大写)叁拾柒亿柒仟贰佰贰拾捌万伍仟柦佰元整",
      "taxRate": "未填写",
      "tax": null
    }
  ]
}

请立即提取并输出JSON。
"""

# ============================================================
# 第二步：金额验算（专注计算）
# ============================================================
PROMPT_PART1_金额验算_STEP2_验算金额 = """
你是专业的数学验算专家。现在需要对已提取的价格信息进行严格验算。

**输入数据：**
{extracted_data}

**验算任务：**
1. 计算所有有效分项的value总和（跳过null和"未填写"）
2. 检查分项总和是否等于合同总价
3. 检查数字与大写金额是否一致
4. 列出所有发现的问题

**计算规则：**
- 只累加value为数字的分项
- value为null或"未填写"的分项不参与计算
- 在心里完成计算后，只输出最终数字结果

**验证规则：**
isPriceConsistent 为 true 需同时满足：
1. 至少有一个分项value为数字
2. 所有数字类型的分项都有taxRate（非"未填写"）
3. 所有数字类型的分项都有tax（非null且非"未填写"）
4. 分项value总和 = contractPriceTotal
5. 数字金额与大写金额一致

**问题描述格式：**
如果有问题，按以下格式列出：
"[分项名]金额未填写; [分项名]税率未填写; [分项名]税率已填写但税金未填写; 合同总价X元与分项合计Y元不符，差额Z元; 数字金额与大写金额不一致"

无问题则为空字符串 ""

**输出格式：**
纯JSON，不要```json```标记，不要任何解释文字

**JSON结构：**
{
  "calculatedSum": 数字（必须是计算好的结果，不能是算式）,
  "isPriceConsistent": true或false,
  "priceInconsistencyDescription": "问题描述或空字符串",
  "calculationDetails": {
    "validComponents": ["参与计算的分项名称"],
    "skippedComponents": ["未参与计算的分项名称"],
    "componentCount": 参与计算的分项数量
  }
}

**错误示例（绝对禁止）：**
{
  "calculatedSum": "27993900 + 3772285700 + 12505400"
}

**正确示例：**
{
  "calculatedSum": 4156799100,
  "isPriceConsistent": false,
  "priceInconsistencyDescription": "建筑安装工程费(含设备购置费)税率未填写; 建筑安装工程费(含设备购置费)税金未填写",
  "calculationDetails": {
    "validComponents": ["设计费(含税)", "建筑安装工程费(含设备购置费)(含税)", "暂列金额(含税)"],
    "skippedComponents": ["暂估价(含税)"],
    "componentCount": 3
  }
}

请立即进行验算并输出JSON。calculatedSum必须是一个纯数字！
"""



# ============================================================================
# 设计合同 - 工期验算提示词（三步式）
# ============================================================================
# ---------- 第一步：提取基础信息 ----------
PROMPT_设计合同_工期基础信息 = """
你是专业的设计合同信息提取专家。请从"工程设计周期"或"合同工期"章节中提取基础工期信息。

**设计合同工期特点：**
- 通常有明确的计划开始设计日期
- 通常有明确的计划完成设计日期
- 可能明确写出总设计周期天数，也可能没有（需要计算）
- 工期单位通常是"日历天"

**提取任务：**
1. 提取计划开始设计日期（原文）
2. 提取计划完成设计日期（原文）
3. 提取总设计周期天数（如果原文有）
4. 识别工期单位

**日期处理规则：**
- 如果是"YYYY年MM月DD日"格式 → 转换为"YYYY-MM-DD"
- 如果是"YYYY-MM-DD"格式 → 直接提取
- 如果是"YYYY年MM月  日" → 提取为"YYYY-MM-XX"
- 如果是"  年  月  日" → 提取为"未填写"
- 如果是"以发包人通知为准" → 提取为"待定"

**输出JSON格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "totalDurationDays": "130 日历天"或null,
  "plannedStartDate": "2020-11-18",
  "plannedCompletionDate": "2021-03-28",
  "unit": "日历天",
  "startDateComplete": true,
  "completionDateComplete": true,
  "durationUnit": "日历天"
}

**示例：**
输入文本：
```
计划开始设计日期：2020年11月18日
计划完成设计日期：2021年3月28日
```

输出：
{
  "totalDurationDays": null,
  "plannedStartDate": "2020-11-18",
  "plannedCompletionDate": "2021-03-28",
  "unit": "日历天",
  "startDateComplete": true,
  "completionDateComplete": true,
  "durationUnit": "日历天"
}

请立即提取并输出JSON。
"""

# ---------- 第二步：提取里程碑 ----------
PROMPT_设计合同_里程碑提取 = """
你是专业的设计合同信息提取专家。请从"工程设计周期"或相关章节中提取所有设计阶段成果提交节点。

**设计合同里程碑特点：**
- 通常有阶段性成果节点：方案设计、初步设计、施工图设计
- 可能有具体的提交日期，也可能只有相对时间描述

**提取任务：**
提取所有设计阶段成果提交节点及时间要求

**输出JSON格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "projectMilestones": [
    {
      "name": "方案设计成果提交",
      "timePoint": "2020年12月15日"或"开工后30日内",
      "description": "完成方案设计及优化，提交方案设计文件"
    },
    {
      "name": "初步设计成果提交",
      "timePoint": "2021年01月20日",
      "description": "完成初步设计，提交初步设计文件及概算"
    },
    {
      "name": "施工图设计成果提交",
      "timePoint": "2021年03月28日",
      "description": "完成施工图设计，提交全套施工图"
    }
  ]
}

**字段说明：**
- `name`: 里程碑简短名称
- `timePoint`: 时间点描述（具体日期或相对时间）
- `description`: 完整描述

**如果没有明确的里程碑节点，返回空数组：**
{
  "projectMilestones": []
}

请立即提取并输出JSON。
"""

# ---------- 第三步：工期验算 ----------
PROMPT_设计合同_工期验算 = """
你是专业的工期验算专家。现在对设计合同工期信息进行验算。

**输入数据：**
基础信息: {basic_info}
里程碑信息: {milestones}

**设计合同验算规则：**
1. 如果开始日期和完成日期都是具体日期 → 计算天数差
2. 如果原文有总设计周期天数 → 与计算天数比对
3. 如果原文没有总设计周期天数 → 只显示计算天数
4. 如果开始日期或完成日期是"待定"或"未填写" → 无法计算

**验算任务：**
1. 计算开始日期到完成日期的天数差
2. 如果原文有总天数，比对是否一致
3. 合并里程碑信息，并自动添加开始和结束节点作为里程碑

**输出JSON格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "duration": {
    "totalDurationDays": "从basic_info获取"或"计算得出的天数 日历天",
    "plannedStartDate": "从basic_info获取",
    "plannedCompletionDate": "从basic_info获取",
    "calculatedDays": "具体天数"或"无法计算（日期不完整）",
    "isDurationConsistent": true或false,
    "durationInconsistencyDescription": "问题描述或空字符串",
    "projectMilestones": [
      {
        "name": "从milestones获取",
        "timePoint": "从milestones获取",
        "deadline": "具体日期"或null,
        "description": "从milestones获取"
      }
    ]
  }
}

**验算逻辑示例：**

**情况1：两个日期都明确，原文无总天数（最常见）**
输入basic_info：
{
  "totalDurationDays": null,
  "plannedStartDate": "2020-11-18",
  "plannedCompletionDate": "2021-03-28",
  "startDateComplete": true,
  "completionDateComplete": true
}

输入milestones：
{
  "projectMilestones": []
}

输出：
{
  "duration": {
    "totalDurationDays": "130 日历天",
    "plannedStartDate": "2020-11-18",
    "plannedCompletionDate": "2021-03-28",
    "calculatedDays": "130",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": [
      {
        "name": "计划开始设计",
        "timePoint": "2020-11-18",
        "deadline": "2020-11-18",
        "description": "计划开始设计日期"
      },
      {
        "name": "计划完成设计",
        "timePoint": "2021-03-28",
        "deadline": "2021-03-28",
        "description": "计划完成设计日期"
      }
    ]
  }
}

**说明：**
从2020-11-18到2021-03-28共130天，原文未写总天数，计算后填入totalDurationDays。
自动添加开始和结束作为里程碑。

**情况2：两个日期都明确，原文有总天数且一致**
输入basic_info：
{
  "totalDurationDays": "130 日历天",
  "plannedStartDate": "2020-11-18",
  "plannedCompletionDate": "2021-03-28",
  "startDateComplete": true,
  "completionDateComplete": true
}

输入milestones：
{
  "projectMilestones": []
}

输出：
{
  "duration": {
    "totalDurationDays": "130 日历天",
    "plannedStartDate": "2020-11-18",
    "plannedCompletionDate": "2021-03-28",
    "calculatedDays": "130",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": [
      {
        "name": "计划开始设计",
        "timePoint": "2020-11-18",
        "deadline": "2020-11-18",
        "description": "计划开始设计日期"
      },
      {
        "name": "计划完成设计",
        "timePoint": "2021-03-28",
        "deadline": "2021-03-28",
        "description": "计划完成设计日期"
      }
    ]
  }
}

**情况2A：有中间里程碑的情况**
输入basic_info：
{
  "totalDurationDays": "130 日历天",
  "plannedStartDate": "2020-11-18",
  "plannedCompletionDate": "2021-03-28",
  "startDateComplete": true,
  "completionDateComplete": true
}

输入milestones：
{
  "projectMilestones": [
    {
      "name": "方案设计成果提交",
      "timePoint": "2020-12-15",
      "description": "完成方案设计"
    },
    {
      "name": "初步设计成果提交",
      "timePoint": "2021-01-20",
      "description": "完成初步设计"
    }
  ]
}

输出：
{
  "duration": {
    "totalDurationDays": "130 日历天",
    "plannedStartDate": "2020-11-18",
    "plannedCompletionDate": "2021-03-28",
    "calculatedDays": "130",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": [
      {
        "name": "计划开始设计",
        "timePoint": "2020-11-18",
        "deadline": "2020-11-18",
        "description": "计划开始设计日期"
      },
      {
        "name": "方案设计成果提交",
        "timePoint": "2020-12-15",
        "deadline": "2020-12-15",
        "description": "完成方案设计"
      },
      {
        "name": "初步设计成果提交",
        "timePoint": "2021-01-20",
        "deadline": "2021-01-20",
        "description": "完成初步设计"
      },
      {
        "name": "计划完成设计",
        "timePoint": "2021-03-28",
        "deadline": "2021-03-28",
        "description": "计划完成设计日期"
      }
    ]
  }
}

**说明：**
开始和结束节点自动添加在里程碑数组的首尾，中间是提取的设计阶段节点，按时间顺序排列。

**情况3：两个日期都明确，原文有总天数但不一致**
输入basic_info：
{
  "totalDurationDays": "120 日历天",
  "plannedStartDate": "2020-11-18",
  "plannedCompletionDate": "2021-03-28",
  "startDateComplete": true,
  "completionDateComplete": true
}

输入milestones：
{
  "projectMilestones": []
}

输出：
{
  "duration": {
    "totalDurationDays": "120 日历天",
    "plannedStartDate": "2020-11-18",
    "plannedCompletionDate": "2021-03-28",
    "calculatedDays": "130",
    "isDurationConsistent": false,
    "durationInconsistencyDescription": "合同约定设计周期120日历天，但根据开始日期(2020-11-18)至完成日期(2021-03-28)计算为130天，相差10天",
    "projectMilestones": [
      {
        "name": "计划开始设计",
        "timePoint": "2020-11-18",
        "deadline": "2020-11-18",
        "description": "计划开始设计日期"
      },
      {
        "name": "计划完成设计",
        "timePoint": "2021-03-28",
        "deadline": "2021-03-28",
        "description": "计划完成设计日期"
      }
    ]
  }
}

**情况4：开始日期待定**
输入basic_info：
{
  "totalDurationDays": "130 日历天",
  "plannedStartDate": "待定",
  "plannedCompletionDate": "未填写",
  "startDateComplete": false,
  "completionDateComplete": false
}

输出：
{
  "duration": {
    "totalDurationDays": "130 日历天",
    "plannedStartDate": "待定",
    "plannedCompletionDate": "未填写",
    "calculatedDays": "开始日期待定",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": []
  }
}

**说明：**
开始日期待定时，不添加开始和结束里程碑（因为没有具体日期）。

**情况5：日期未填写**
输入basic_info：
{
  "totalDurationDays": "130 日历天",
  "plannedStartDate": "未填写",
  "plannedCompletionDate": "未填写",
  "startDateComplete": false,
  "completionDateComplete": false
}

输出：
{
  "duration": {
    "totalDurationDays": "130 日历天",
    "plannedStartDate": "未填写",
    "plannedCompletionDate": "未填写",
    "calculatedDays": "无法计算（日期不完整）",
    "isDurationConsistent": false,
    "durationInconsistencyDescription": "计划开始日期未填写; 计划完成日期未填写",
    "projectMilestones": []
  }
}

**说明：**
日期未填写时，不添加开始和结束里程碑（因为没有具体日期）。

**里程碑处理规则（重要）：**
1. 自动添加开始节点：如果plannedStartDate是具体日期，在里程碑数组开头添加"计划开始设计"节点
2. 自动添加结束节点：如果plannedCompletionDate是具体日期，在里程碑数组末尾添加"计划完成设计"节点
3. 合并中间节点：将milestones中的设计阶段节点插入开始和结束之间
4. 按时间排序：确保里程碑按时间顺序排列（开始 → 中间阶段 → 结束）
5. deadline计算：
   - 如果timePoint是具体日期（如"2021-01-20"） → deadline直接使用该日期
   - 如果timePoint是相对时间（如"开工后30日内"）且plannedStartDate是具体日期 → 计算deadline
   - 如果plannedStartDate是"待定"或"未填写" → deadline设为null

请立即验算并输出JSON。
"""



# ============================================================================
# 设计合同 - 金额验算提示词（两步式）
# ============================================================================
# ---------- 第一步：提取价格信息 ----------
PROMPT_设计合同_金额提取 = """
你是专业的设计合同信息提取专家。请从"合同价格形式与签约合同价"章节中提取所有价格相关信息。

**设计合同价格特点：**
- 通常是固定总价或单价合同
- 通常只有签约合同价，无分项明细（设计费一般不细分）
- 重点：合同总价、大写金额、价格形式

**任务要求：**
1. 提取合同价格形式（固定总价/单价合同等）
2. 提取签约合同价（数字）
3. 提取签约合同价（大写）
4. 判断是否有分项（设计合同通常无分项）
5. 只提取信息，不做计算验证

**金额格式处理：**
- 提取纯数字，保留小数点
- 例如："¥10588800.00元" → 提取为 10588800
- 例如："壹仟零伍拾捌万捌仟捌佰元整" → 原样提取大写

**输出格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "contractPriceTotal": 10588800,
  "contractPriceTotalChinese": "壹仟零伍拾捌万捌仟捌佰元整",
  "priceFormType": "固定总价",
  "components": []
}

**示例1：固定总价，无分项（最常见）**
输入文本：
```
合同价格形式：固定总价
签约合同价为：人民币（大写）壹仟零伍拾捌万捌仟捌佰元整（¥10588800.00元）
```

输出：
{
  "contractPriceTotal": 10588800,
  "contractPriceTotalChinese": "壹仟零伍拾捌万捌仟捌佰元整",
  "priceFormType": "固定总价",
  "components": []
}

**示例2：单价合同，可能有简单分项**
输入文本：
```
合同价格形式：单价合同
签约合同价为：人民币（大写）伍佰万元整（¥5000000元）
其中：方案设计费：200万元
      初步设计费：150万元
      施工图设计费：150万元
```

输出：
{
  "contractPriceTotal": 5000000,
  "contractPriceTotalChinese": "伍佰万元整",
  "priceFormType": "单价合同",
  "components": [
    {
      "name": "方案设计费",
      "value": 2000000,
      "chinese": "未填写",
      "taxRate": "未填写",
      "tax": null
    },
    {
      "name": "初步设计费",
      "value": 1500000,
      "chinese": "未填写",
      "taxRate": "未填写",
      "tax": null
    },
    {
      "name": "施工图设计费",
      "value": 1500000,
      "chinese": "未填写",
      "taxRate": "未填写",
      "tax": null
    }
  ]
}

**注意事项：**
- 如果只有签约合同价，无任何分项 → components为空数组[]
- 如果有分项（如不同阶段的设计费），提取到components数组
- 设计合同的分项通常没有税率、税金 → taxRate填"未填写"，tax填null
- 只提取信息，不做验算

请立即提取并输出JSON。
"""

# ---------- 第二步：金额验算 ----------
PROMPT_设计合同_金额验算 = """
你是专业的数学验算专家。现在对设计合同价格信息进行验算。

**输入数据：**
{extracted_data}

**设计合同验算规则：**
设计合同通常只有签约合同价，无分项明细，这是正常现象。
验算重点：
1. 如果无分项 → 验证数字与大写是否一致
2. 如果有分项 → 验证分项总和是否等于合同总价，且数字与大写是否一致

**计算规则：**
- 只累加value为数字的分项
- value为null的分项跳过

**isPriceConsistent判定规则：**

情况A：无分项合同（components为空数组）
  - calculatedSum = contractPriceTotal
  - 如果数字金额与大写金额一致 → isPriceConsistent = true
  - 如果数字金额与大写金额不一致 → isPriceConsistent = false
  - priceInconsistencyDescription = 问题描述或空字符串

情况B：有分项合同
  - calculatedSum = 所有分项value的总和
  - 验证1：分项总和是否等于contractPriceTotal
  - 验证2：数字金额与大写金额是否一致
  - 如果都一致 → isPriceConsistent = true
  - 如果任一不一致 → isPriceConsistent = false
  - 设计合同的分项可以没有taxRate和tax，不影响一致性判定

**输出格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "calculatedSum": 数字（纯数字，不能是算式）,
  "isPriceConsistent": true或false,
  "priceInconsistencyDescription": "问题描述或空字符串",
  "calculationDetails": {
    "validComponents": ["参与计算的分项名称"],
    "skippedComponents": ["未参与计算的分项名称"],
    "componentCount": 参与计算的分项数量
  }
}

**示例1：无分项且一致（最常见）**
输入：
{
  "contractPriceTotal": 10588800,
  "contractPriceTotalChinese": "壹仟零伍拾捌万捌仟捌佰元整",
  "priceFormType": "固定总价",
  "components": []
}

输出：
{
  "calculatedSum": 10588800,
  "isPriceConsistent": true,
  "priceInconsistencyDescription": "",
  "calculationDetails": {
    "validComponents": [],
    "skippedComponents": [],
    "componentCount": 0
  }
}

**示例2：无分项但数字与大写不一致**
输入：
{
  "contractPriceTotal": 10588800,
  "contractPriceTotalChinese": "壹仟零伍拾捌万元整",
  "priceFormType": "固定总价",
  "components": []
}

输出：
{
  "calculatedSum": 10588800,
  "isPriceConsistent": false,
  "priceInconsistencyDescription": "数字金额10588800元与大写金额'壹仟零伍拾捌万元整'(10580000元)不一致",
  "calculationDetails": {
    "validComponents": [],
    "skippedComponents": [],
    "componentCount": 0
  }
}

**示例3：有分项且一致**
输入：
{
  "contractPriceTotal": 5000000,
  "contractPriceTotalChinese": "伍佰万元整",
  "priceFormType": "单价合同",
  "components": [
    {"name": "方案设计费", "value": 2000000, "taxRate": "未填写", "tax": null},
    {"name": "初步设计费", "value": 1500000, "taxRate": "未填写", "tax": null},
    {"name": "施工图设计费", "value": 1500000, "taxRate": "未填写", "tax": null}
  ]
}

输出：
{
  "calculatedSum": 5000000,
  "isPriceConsistent": true,
  "priceInconsistencyDescription": "",
  "calculationDetails": {
    "validComponents": ["方案设计费", "初步设计费", "施工图设计费"],
    "skippedComponents": [],
    "componentCount": 3
  }
}

**示例4：有分项但总和不一致**
输入：
{
  "contractPriceTotal": 5500000,
  "contractPriceTotalChinese": "伍佰伍拾万元整",
  "priceFormType": "单价合同",
  "components": [
    {"name": "方案设计费", "value": 2000000, "taxRate": "未填写", "tax": null},
    {"name": "初步设计费", "value": 1500000, "taxRate": "未填写", "tax": null},
    {"name": "施工图设计费", "value": 1500000, "taxRate": "未填写", "tax": null}
  ]
}

输出：
{
  "calculatedSum": 5000000,
  "isPriceConsistent": false,
  "priceInconsistencyDescription": "合同总价5500000元与分项合计5000000元不符，差额500000元",
  "calculationDetails": {
    "validComponents": ["方案设计费", "初步设计费", "施工图设计费"],
    "skippedComponents": [],
    "componentCount": 3
  }
}

请立即验算并输出JSON。calculatedSum必须是纯数字！
"""



# ============================================================
# 勘察合同 - 工期验算提示词（三步式）
# ============================================================
# ---------- 第一步：提取基础信息 ----------
PROMPT_勘察合同_工期基础信息 = """
你是专业的合同信息提取专家。请从"合同工期"章节中提取基础工期信息。

**勘察合同特点：**
- 开工日期可能是待定（以发包人指令为准）
- 开工日期也可能是具体日期
- 通常只有工期总天数，不一定有竣工日期

**提取任务：**
1. 提取工期总天数（原文）
2. 提取开工日期（原文是什么就提取什么）
3. 提取竣工日期（如果有）
4. 识别工期单位

**日期处理规则（非常重要）：**
- 如果原文是"以发包人下达的开工指令为准"或类似表述 → 提取为"待定"
- 如果原文是"以监理工程师指令为准"或类似表述 → 提取为"待定"
- 如果是"YYYY-MM-DD"格式的具体日期 → 直接提取
- 如果是"YYYY年MM月  日"（日期不完整） → 提取为"YYYY-MM-XX"
- 如果是"  年  月  日"（完全空白） → 提取为"未填写"

**关键区分：**
"待定" = 合同明确约定由发包人/监理决定开工时间（正常条款）
"未填写" = 合同应填但未填的空白（合同缺陷）

**输出JSON格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "totalDurationDays": "30 日历天",
  "plannedStartDate": "待定"或"2021-09-15"或"未填写",
  "plannedCompletionDate": "未填写"或具体日期,
  "unit": "日历天",
  "startDateComplete": true或false,
  "completionDateComplete": true或false,
  "durationUnit": "日历天"
}

**示例1：待定开工日期**
{
  "totalDurationDays": "30 日历天",
  "plannedStartDate": "待定",
  "plannedCompletionDate": "未填写",
  "unit": "日历天",
  "startDateComplete": false,
  "completionDateComplete": false,
  "durationUnit": "日历天"
}

**示例2：具体开工日期**
{
  "totalDurationDays": "60 日历天",
  "plannedStartDate": "2024-01-15",
  "plannedCompletionDate": "未填写",
  "unit": "日历天",
  "startDateComplete": true,
  "completionDateComplete": false,
  "durationUnit": "日历天"
}

请立即提取并输出JSON。
"""

# ---------- 第二步：提取里程碑 ----------
PROMPT_勘察合同_里程碑提取 = """
你是专业的合同信息提取专家。请从"合同工期"章节中提取所有成果提交节点。

**勘察合同特点：**
勘察合同通常有多个成果提交节点，如：初步勘察报告、详细勘察报告等。

**提取任务：**
提取所有成果提交时间节点及要求

**输出JSON格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "projectMilestones": [
    {
      "name": "提交初步勘察报告",
      "timePoint": "开工10日内",
      "description": "勘察人在开工10日内向发包人提交初步勘察报告"
    },
    {
      "name": "提交详细勘察报告",
      "timePoint": "开工20日内",
      "description": "勘察人在开工20日内向发包人提交详细勘察报告"
    }
  ]
}

**字段说明：**
- `name`: 里程碑简短名称
- `timePoint`: 时间点描述（如"开工10日内"）
- `description`: 完整描述

**如果没有里程碑，返回空数组：**
{
  "projectMilestones": []
}

请立即提取并输出JSON。
"""

# ---------- 第三步：工期验算 ----------
PROMPT_勘察合同_工期验算 = """
你是专业的工期验算专家。现在对勘察合同工期信息进行验算。

**输入数据：**
基础信息: {basic_info}
里程碑信息: {milestones}

**勘察合同验算规则（非常重要）：**
1. 如果开工日期是"待定"（以发包人指令为准） → 这是勘察合同的标准条款，isDurationConsistent = true
2. 如果开工日期是具体日期且竣工日期也是具体日期 → 计算天数差并比对
3. 如果开工日期"未填写"（空白未填） → isDurationConsistent = false

**关键判断：待定 ≠ 未填写**
- "待定"是明确的合同约定，表示开工时间由发包人决定，这是正常的
- "未填写"是合同存在缺陷，应该填但没填

**验算任务：**
1. 判断开工日期类型（待定/具体日期/未填写）
2. 根据不同类型采用不同验算逻辑
3. 合并里程碑信息

**isDurationConsistent判定逻辑：**
- plannedStartDate = "待定" 且 totalDurationDays存在 → isDurationConsistent = true
- plannedStartDate = 具体日期 且 plannedCompletionDate = 具体日期 且 天数一致 → isDurationConsistent = true
- plannedStartDate = 具体日期 且 plannedCompletionDate = 具体日期 且 天数不一致 → isDurationConsistent = false
- plannedStartDate = 具体日期 且 plannedCompletionDate = "未填写" → isDurationConsistent = true（只要有总工期）
- plannedStartDate = "未填写" → isDurationConsistent = false

**输出JSON格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "duration": {
    "totalDurationDays": "从basic_info获取",
    "plannedStartDate": "从basic_info获取",
    "plannedCompletionDate": "从basic_info获取",
    "calculatedDays": "开工日期待定"或"具体天数"或"无法计算（日期不完整）",
    "isDurationConsistent": true或false,
    "durationInconsistencyDescription": "问题描述或空字符串",
    "projectMilestones": [
      {
        "name": "从milestones获取",
        "timePoint": "从milestones获取",
        "deadline": null或"具体日期",
        "description": "从milestones获取"
      }
    ]
  }
}

**验算逻辑示例：**

**情况1：开工日期待定（勘察合同最常见，验算通过）**
输入basic_info：
{
  "totalDurationDays": "30 日历天",
  "plannedStartDate": "待定",
  "plannedCompletionDate": "未填写"
}

输出：
{
  "duration": {
    "totalDurationDays": "30 日历天",
    "plannedStartDate": "待定",
    "plannedCompletionDate": "未填写",
    "calculatedDays": "开工日期待定",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": [
      {
        "name": "提交初步勘察报告",
        "timePoint": "开工10日内",
        "deadline": null,
        "description": "勘察人在开工10日内向发包人提交初步勘察报告"
      },
      {
        "name": "提交详细勘察报告",
        "timePoint": "开工20日内",
        "deadline": null,
        "description": "勘察人在开工20日内向发包人提交详细勘察报告"
      }
    ]
  }
}

**说明：**
这是你提供的案例，开工日期"以发包人下达的开工指令为准"是正常合同条款。
只要有总工期天数，就应该验算通过（isDurationConsistent = true）。

**情况2：开工日期具体但竣工日期未填写**
输入basic_info：
{
  "totalDurationDays": "60 日历天",
  "plannedStartDate": "2024-01-15",
  "plannedCompletionDate": "未填写"
}

输出：
{
  "duration": {
    "totalDurationDays": "60 日历天",
    "plannedStartDate": "2024-01-15",
    "plannedCompletionDate": "未填写",
    "calculatedDays": "无法计算（竣工日期未填写）",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": [...]
  }
}

**情况3：两个日期都具体且一致**
输入basic_info：
{
  "totalDurationDays": "60 日历天",
  "plannedStartDate": "2024-01-15",
  "plannedCompletionDate": "2024-03-15"
}

输出：
{
  "duration": {
    "totalDurationDays": "60 日历天",
    "plannedStartDate": "2024-01-15",
    "plannedCompletionDate": "2024-03-15",
    "calculatedDays": "60",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": [...]
  }
}

**情况4：两个日期都具体但不一致**
输入basic_info：
{
  "totalDurationDays": "60 日历天",
  "plannedStartDate": "2024-01-15",
  "plannedCompletionDate": "2024-03-20"
}

输出：
{
  "duration": {
    "totalDurationDays": "60 日历天",
    "plannedStartDate": "2024-01-15",
    "plannedCompletionDate": "2024-03-20",
    "calculatedDays": "65",
    "isDurationConsistent": false,
    "durationInconsistencyDescription": "合同约定工期60日历天，但根据开工日期(2024-01-15)至竣工日期(2024-03-20)计算为65天，相差5天",
    "projectMilestones": [...]
  }
}

**情况5：开工日期未填写（合同缺陷，验算不通过）**
输入basic_info：
{
  "totalDurationDays": "60 日历天",
  "plannedStartDate": "未填写",
  "plannedCompletionDate": "未填写"
}

输出：
{
  "duration": {
    "totalDurationDays": "60 日历天",
    "plannedStartDate": "未填写",
    "plannedCompletionDate": "未填写",
    "calculatedDays": "无法计算（日期不完整）",
    "isDurationConsistent": false,
    "durationInconsistencyDescription": "计划开始日期未填写; 计划竣工日期未填写",
    "projectMilestones": [...]
  }
}

**对比说明：**
- "待定"（情况1）= 正常合同条款 → isDurationConsistent = true
- "未填写"（情况5）= 合同缺陷 → isDurationConsistent = false

**里程碑deadline计算规则：**
- 如果plannedStartDate是具体日期 → 可以计算deadline
- 如果plannedStartDate是"待定"或"未填写" → deadline设为null

请立即验算并输出JSON。
"""


#============================================================
# 勘察合同 - 金额验算提示词（两步式）
# ============================================================
# ---------- 第一步：提取价格信息 ----------
PROMPT_勘察合同_金额提取 = """
你是专业的合同信息提取专家。请从"合同价款"章节中提取所有价格相关信息。

**勘察合同特点：**
- 可能只有总价，无分项
- 可能有简单分项（如不同地块的勘察费）
- 分项通常不包含税率、税金明细

**任务要求：**
1. 提取合同总价（数字和大写）
2. 提取价格形式
3. 提取所有分项（如果有）
4. 只提取信息，不做计算验证

**分项识别规则：**
- 如果合同明确列出"XX地块勘察费"等分项，提取到components数组
- 如果只有总价无分项，components为空数组[]
- 分项的taxRate和tax通常为"未填写"或null

**输出格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "contractPriceTotal": 数字或null,
  "contractPriceTotalChinese": "大写或未填写",
  "priceFormType": "价格形式或未填写",
  "components": [
    {
      "name": "分项名称",
      "value": 数字或null,
      "chinese": "大写或未填写",
      "taxRate": "未填写",
      "tax": null
    }
  ]
}

**示例1：无分项**
{
  "contractPriceTotal": 394373.2,
  "contractPriceTotalChinese": "叁拾玖万肆仟叁佰柒拾叁元贰角",
  "priceFormType": "总价合同",
  "components": []
}

**示例2：有简单分项**
{
  "contractPriceTotal": 396740,
  "contractPriceTotalChinese": "叁拾玖万陆仟柒佰肆拾元整",
  "priceFormType": "单价合同",
  "components": [
    {
      "name": "浦乐单元R21-2la(1)地块勘察费",
      "value": 282160,
      "chinese": "未填写",
      "taxRate": "未填写",
      "tax": null
    },
    {
      "name": "浦乐单元R21-21a(2)地块勘察费",
      "value": 114580,
      "chinese": "未填写",
      "taxRate": "未填写",
      "tax": null
    }
  ]
}

请立即提取并输出JSON。
"""

# ---------- 第二步：金额验算 ----------
PROMPT_勘察合同_金额验算 = """
你是专业的数学验算专家。现在对勘察合同价格信息进行验算。

**输入数据：**
{extracted_data}

**勘察合同验算规则：**
勘察合同的分项通常不包含税率、税金明细，这是正常现象。
验算重点：分项总和是否等于合同总价。

**验算任务：**
1. 如果components为空数组 → 无分项合同
2. 如果components有数据 → 计算分项总和
3. 检查分项总和是否等于合同总价
4. 勘察合同不强制要求taxRate和tax

**计算规则：**
- 只累加value为数字的分项
- value为null的分项跳过

**isPriceConsistent判定规则：**

情况A：无分项合同（components为空数组）
  - calculatedSum = contractPriceTotal
  - isPriceConsistent = true
  - priceInconsistencyDescription = ""

情况B：有分项合同
  - calculatedSum = 所有分项value的总和
  - 如果分项总和 = contractPriceTotal → isPriceConsistent = true
  - 如果分项总和 ≠ contractPriceTotal → isPriceConsistent = false
  - 勘察合同的分项可以没有taxRate和tax，不影响一致性判定

**输出格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "calculatedSum": 数字（纯数字，不能是算式）,
  "isPriceConsistent": true或false,
  "priceInconsistencyDescription": "问题描述或空字符串",
  "calculationDetails": {
    "validComponents": ["参与计算的分项名称"],
    "skippedComponents": ["未参与计算的分项名称"],
    "componentCount": 参与计算的分项数量
  }
}

**示例1：无分项合同**
输入：
{
  "contractPriceTotal": 394373.2,
  "components": []
}

输出：
{
  "calculatedSum": 394373.2,
  "isPriceConsistent": true,
  "priceInconsistencyDescription": "",
  "calculationDetails": {
    "validComponents": [],
    "skippedComponents": [],
    "componentCount": 0
  }
}

**示例2：有分项且一致**
输入：
{
  "contractPriceTotal": 396740,
  "components": [
    {"name": "浦乐单元R21-2la(1)地块勘察费", "value": 282160, "taxRate": "未填写", "tax": null},
    {"name": "浦乐单元R21-21a(2)地块勘察费", "value": 114580, "taxRate": "未填写", "tax": null}
  ]
}

输出：
{
  "calculatedSum": 396740,
  "isPriceConsistent": true,
  "priceInconsistencyDescription": "",
  "calculationDetails": {
    "validComponents": ["浦乐单元R21-2la(1)地块勘察费", "浦乐单元R21-21a(2)地块勘察费"],
    "skippedComponents": [],
    "componentCount": 2
  }
}

**示例3：有分项但不一致**
输入：
{
  "contractPriceTotal": 400000,
  "components": [
    {"name": "地块1勘察费", "value": 282160, "taxRate": "未填写", "tax": null},
    {"name": "地块2勘察费", "value": 114580, "taxRate": "未填写", "tax": null}
  ]
}

输出：
{
  "calculatedSum": 396740,
  "isPriceConsistent": false,
  "priceInconsistencyDescription": "合同总价400000元与分项合计396740元不符，差额3260元",
  "calculationDetails": {
    "validComponents": ["地块1勘察费", "地块2勘察费"],
    "skippedComponents": [],
    "componentCount": 2
  }
}

请立即验算并输出JSON。calculatedSum必须是纯数字！
"""




# ============================================================================
# 监理合同 - 工期验算提示词（三步式）
# ============================================================================
# ---------- 第一步：提取基础信息 ----------
PROMPT_监理合同_工期基础信息 = """
你是专业的监理合同信息提取专家。请从"监理服务期"或"合同期限"章节中提取基础工期信息。

**监理合同工期特点：**
- 开始日期通常是空白（如"2023年_月_日"），具体以开工令为准
- 完成日期通常是空白（如"_年_月_日"），具体以竣工报告为准
- 必定有明确的总监理服务期天数（如2230日历天）
- 可能包含分段信息（如缺陷责任期730日历天）

**提取任务：**
1. 提取总监理服务期天数（含单位）
2. 提取合同开始日期（原文）
3. 提取合同完成日期（原文）
4. 提取是否有分段（如缺陷责任期）

**日期处理规则：**
- 如果是"2023年_月_日"或"_年_月_日"（空白） → 提取为"未填写"
- 如果是"YYYY年MM月DD日"格式 → 转换为"YYYY-MM-DD"
- 如果是"YYYY-MM-DD"格式 → 直接提取
- 如果写明"以开工令为准"或"以竣工报告为准" → 提取为"待定"

**输出JSON格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "totalDurationDays": "2230 日历天",
  "plannedStartDate": "未填写"或"待定"或具体日期,
  "plannedCompletionDate": "未填写"或"待定"或具体日期,
  "unit": "日历天",
  "startDateComplete": false,
  "completionDateComplete": false,
  "durationUnit": "日历天",
  "additionalInfo": {
    "defectLiabilityPeriod": "730 日历天"或null,
    "startBasedOn": "开工令"或null,
    "endBasedOn": "竣工报告"或null
  }
}

**示例1：典型监理合同（日期空白）**
输入文本：
```
本合同自2023年_月_日开始实施，计划至_年_月_日完成。
监理服务期总计2230日历天，其中缺陷责任期为730日历天。
具体时间以开工令和竣工报告为准。
```

输出：
{
  "totalDurationDays": "2230 日历天",
  "plannedStartDate": "未填写",
  "plannedCompletionDate": "未填写",
  "unit": "日历天",
  "startDateComplete": false,
  "completionDateComplete": false,
  "durationUnit": "日历天",
  "additionalInfo": {
    "defectLiabilityPeriod": "730 日历天",
    "startBasedOn": "开工令",
    "endBasedOn": "竣工报告"
  }
}

**示例2：有具体日期的监理合同（少见）**
输入文本：
```
本合同自2023年6月1日开始实施，计划至2029年7月15日完成。
监理服务期总计2230日历天。
```

输出：
{
  "totalDurationDays": "2230 日历天",
  "plannedStartDate": "2023-06-01",
  "plannedCompletionDate": "2029-07-15",
  "unit": "日历天",
  "startDateComplete": true,
  "completionDateComplete": true,
  "durationUnit": "日历天",
  "additionalInfo": {
    "defectLiabilityPeriod": null,
    "startBasedOn": null,
    "endBasedOn": null
  }
}

请立即提取并输出JSON。
"""

# ---------- 第二步：提取里程碑 ----------
PROMPT_监理合同_里程碑提取 = """
你是专业的监理合同信息提取专家。请从"监理服务期"或相关章节中提取所有监理服务阶段节点。

**监理合同里程碑特点：**
- 可能有施工阶段监理、缺陷责任期监理等分段
- 里程碑通常是相对时间（如"缺陷责任期730天"）而非具体日期

**提取任务：**
提取所有监理服务阶段节点及时间要求

**输出JSON格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "projectMilestones": [
    {
      "name": "施工阶段监理",
      "timePoint": "1500 日历天"或"开工令至竣工验收",
      "description": "施工阶段监理服务"
    },
    {
      "name": "缺陷责任期监理",
      "timePoint": "730 日历天",
      "description": "缺陷责任期监理服务"
    }
  ]
}

**字段说明：**
- `name`: 里程碑简短名称
- `timePoint`: 时间点描述（相对时间或时间段）
- `description`: 完整描述

**如果没有明确的里程碑节点，返回空数组：**
{
  "projectMilestones": []
}

**提取原则：**
- 如果原文提到"缺陷责任期"，提取为一个里程碑
- 如果原文提到其他阶段（如"施工准备期"、"竣工验收阶段"），也提取
- 如果没有任何阶段划分，返回空数组

请立即提取并输出JSON。
"""

# ---------- 第三步：工期验算 ----------
PROMPT_监理合同_工期验算 = """
你是专业的工期验算专家。现在对监理合同工期信息进行验算。

**输入数据：**
基础信息: {basic_info}
里程碑信息: {milestones}

**监理合同验算规则（重要）：**
1. 监理合同的开始和完成日期通常是空白（未填写），因为具体时间以开工令和竣工报告为准
2. 只要有明确的总监理服务期天数，就认为工期条款完整
3. 如果有具体日期，才进行日期验算

**验算任务：**
1. 判断日期是否填写
2. 如果有具体日期，计算天数差并与总服务期比对
3. 如果日期未填写但有总服务期，标记为正常
4. 合并里程碑信息

**输出JSON格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "duration": {
    "totalDurationDays": "从basic_info获取",
    "plannedStartDate": "从basic_info获取",
    "plannedCompletionDate": "从basic_info获取",
    "calculatedDays": "日期未填写（以开工令和竣工报告为准）"或具体天数,
    "isDurationConsistent": true或false,
    "durationInconsistencyDescription": "问题描述或空字符串",
    "projectMilestones": [
      {
        "name": "从milestones获取",
        "timePoint": "从milestones获取",
        "deadline": null,
        "description": "从milestones获取"
      }
    ]
  }
}

**验算逻辑示例：**

**情况1：日期未填写但有总服务期（最常见，验算通过）**
输入basic_info：
{
  "totalDurationDays": "2230 日历天",
  "plannedStartDate": "未填写",
  "plannedCompletionDate": "未填写",
  "startDateComplete": false,
  "completionDateComplete": false,
  "additionalInfo": {
    "defectLiabilityPeriod": "730 日历天",
    "startBasedOn": "开工令",
    "endBasedOn": "竣工报告"
  }
}

输入milestones：
{
  "projectMilestones": [
    {
      "name": "缺陷责任期监理",
      "timePoint": "730 日历天",
      "description": "缺陷责任期监理服务"
    }
  ]
}

输出：
{
  "duration": {
    "totalDurationDays": "2230 日历天",
    "plannedStartDate": "未填写",
    "plannedCompletionDate": "未填写",
    "calculatedDays": "日期未填写（以开工令和竣工报告为准）",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": [
      {
        "name": "缺陷责任期监理",
        "timePoint": "730 日历天",
        "deadline": null,
        "description": "缺陷责任期监理服务"
      }
    ]
  }
}

**说明：**
监理合同的日期未填写是正常情况（以开工令和竣工报告为准），只要有总服务期2230天，就验算通过。

**情况2：有具体日期且一致（少见）**
输入basic_info：
{
  "totalDurationDays": "2230 日历天",
  "plannedStartDate": "2023-06-01",
  "plannedCompletionDate": "2029-07-15",
  "startDateComplete": true,
  "completionDateComplete": true,
  "additionalInfo": {
    "defectLiabilityPeriod": null,
    "startBasedOn": null,
    "endBasedOn": null
  }
}

输入milestones：
{
  "projectMilestones": []
}

输出：
{
  "duration": {
    "totalDurationDays": "2230 日历天",
    "plannedStartDate": "2023-06-01",
    "plannedCompletionDate": "2029-07-15",
    "calculatedDays": "2236",
    "isDurationConsistent": false,
    "durationInconsistencyDescription": "合同约定监理服务期2230日历天，但根据开始日期(2023-06-01)至完成日期(2029-07-15)计算为2236天，相差6天",
    "projectMilestones": []
  }
}

**情况3：有具体日期且一致**
输入basic_info：
{
  "totalDurationDays": "2230 日历天",
  "plannedStartDate": "2023-06-01",
  "plannedCompletionDate": "2029-07-09",
  "startDateComplete": true,
  "completionDateComplete": true
}

输出：
{
  "duration": {
    "totalDurationDays": "2230 日历天",
    "plannedStartDate": "2023-06-01",
    "plannedCompletionDate": "2029-07-09",
    "calculatedDays": "2230",
    "isDurationConsistent": true,
    "durationInconsistencyDescription": "",
    "projectMilestones": []
  }
}

**情况4：没有总服务期天数（异常）**
输入basic_info：
{
  "totalDurationDays": null,
  "plannedStartDate": "未填写",
  "plannedCompletionDate": "未填写",
  "startDateComplete": false,
  "completionDateComplete": false
}

输出：
{
  "duration": {
    "totalDurationDays": "未填写",
    "plannedStartDate": "未填写",
    "plannedCompletionDate": "未填写",
    "calculatedDays": "无法计算（总服务期和日期均未填写）",
    "isDurationConsistent": false,
    "durationInconsistencyDescription": "总监理服务期天数未填写",
    "projectMilestones": []
  }
}

**里程碑处理规则：**
- 监理合同的里程碑通常是相对时间（如"缺陷责任期730天"），不是具体日期
- deadline字段固定为null（因为里程碑是相对时间）
- 直接从milestones合并到输出，不需要添加开始和结束节点

请立即验算并输出JSON。
"""




# ============================================================================
# 监理合同 - 金额验算提示词（两步式）
# ============================================================================
# ---------- 第一步：提取价格信息 ----------
PROMPT_监理合同_金额提取 = """
你是专业的监理合同信息提取专家。请从"签约酬金"或"监理服务费"章节中提取所有价格相关信息。

**监理合同价格特点：**
- 签约酬金（监理费）是合同总价
- 可能包含分项（如公共租赁房部分、共有产权房部分）
- 可能包含两部分：监理酬金 + 相关服务酬金
- 通常注明含税价和税率

**任务要求：**
1. 提取签约酬金总额（数字和大写）
2. 提取税率（如果有）
3. 提取分项（如果有不同部分的酬金拆分）
4. 提取监理酬金和相关服务酬金（如果分开列示）
5. 只提取信息，不做计算验证

**分项识别规则：**
- 如果合同列出"公共租赁房部分XX元，共有产权房部分XX元"等分项，提取到components数组
- 如果只有签约酬金总额，无分项，components为空数组[]
- 监理合同的分项通常只有金额，没有税率、税金明细（税已包含在总价中）

**金额格式处理：**
- 提取纯数字，保留小数点
- 例如："¥10520000元" → 提取为 10520000
- 例如："764.5300万元" → 转换为 7645300（统一为元）
- 例如："壹仟零伍拾贰万元整" → 原样提取大写

**输出格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "contractPriceTotal": 10520000,
  "contractPriceTotalChinese": "壹仟零伍拾贰万元整",
  "priceFormType": "固定总价"或"单价合同",
  "components": [
    {
      "name": "分项名称",
      "value": 数字,
      "chinese": "大写或未填写",
      "taxRate": "6%"或"未填写",
      "tax": null
    }
  ]
}

**示例1：有分项的监理合同（最常见）**
输入文本：
```
签约酬金（含税价，税率6%）大写：壹仟零伍拾贰万元整（¥10520000元）
其中公共租赁房部分764.5300万元，共有产权房部分287.4700万元
包括：
1. 监理酬金：¥10520000元
2. 相关服务酬金：/
```

输出：
{
  "contractPriceTotal": 10520000,
  "contractPriceTotalChinese": "壹仟零伍拾贰万元整",
  "priceFormType": "固定总价",
  "components": [
    {
      "name": "公共租赁房部分监理酬金",
      "value": 7645300,
      "chinese": "未填写",
      "taxRate": "6%",
      "tax": null
    },
    {
      "name": "共有产权房部分监理酬金",
      "value": 2874700,
      "chinese": "未填写",
      "taxRate": "6%",
      "taxRate": null
    }
  ]
}

**示例2：监理酬金+相关服务酬金分开列示**
输入文本：
```
签约酬金（含税价，税率6%）：¥10520000元
包括：
1. 监理酬金：¥9000000元
2. 相关服务酬金：¥1520000元
```

输出：
{
  "contractPriceTotal": 10520000,
  "contractPriceTotalChinese": "未填写",
  "priceFormType": "固定总价",
  "components": [
    {
      "name": "监理酬金",
      "value": 9000000,
      "chinese": "未填写",
      "taxRate": "6%",
      "tax": null
    },
    {
      "name": "相关服务酬金",
      "value": 1520000,
      "chinese": "未填写",
      "taxRate": "6%",
      "tax": null
    }
  ]
}

**示例3：无分项的监理合同**
输入文本：
```
签约酬金（含税价，税率6%）大写：壹仟零伍拾贰万元整（¥10520000元）
```

输出：
{
  "contractPriceTotal": 10520000,
  "contractPriceTotalChinese": "壹仟零伍拾贰万元整",
  "priceFormType": "固定总价",
  "components": []
}

**注意事项：**
- 如果金额单位是"万元"，统一转换为"元"（万元 × 10000）
- 如果"相关服务酬金"显示为"/"或"无"，不提取为分项
- taxRate如果原文有写（如6%），所有分项都填写该税率
- tax字段固定为null（监理合同通常不单列税金）
- 只提取信息，不做验算

请立即提取并输出JSON。
"""


# ---------- 第二步：金额验算 ----------
PROMPT_监理合同_金额验算 = """
你是专业的数学验算专家。现在对监理合同价格信息进行验算。

**输入数据：**
{extracted_data}

**监理合同验算规则：**
监理合同可能有分项（如不同部分的监理酬金、监理酬金+相关服务酬金），也可能无分项。
验算重点：
1. 如果无分项 → 验证数字与大写是否一致
2. 如果有分项 → 验证分项总和是否等于签约酬金总额，且数字与大写是否一致

**计算规则：**
- 只累加value为数字的分项
- value为null的分项跳过

**isPriceConsistent判定规则：**

情况A：无分项合同（components为空数组）
  - calculatedSum = contractPriceTotal
  - 如果数字金额与大写金额一致 → isPriceConsistent = true
  - 如果数字金额与大写金额不一致 → isPriceConsistent = false

情况B：有分项合同
  - calculatedSum = 所有分项value的总和
  - 验证1：分项总和是否等于contractPriceTotal
  - 验证2：数字金额与大写金额是否一致
  - 如果都一致 → isPriceConsistent = true
  - 如果任一不一致 → isPriceConsistent = false
  - 监理合同的分项可以没有tax字段，不影响一致性判定

**输出格式：**
纯JSON，不要```json```标记，不要任何解释

**JSON结构：**
{
  "calculatedSum": 数字（纯数字，不能是算式）,
  "isPriceConsistent": true或false,
  "priceInconsistencyDescription": "问题描述或空字符串",
  "calculationDetails": {
    "validComponents": ["参与计算的分项名称"],
    "skippedComponents": ["未参与计算的分项名称"],
    "componentCount": 参与计算的分项数量
  }
}

**示例1：有分项且一致**
输入：
{
  "contractPriceTotal": 10520000,
  "contractPriceTotalChinese": "壹仟零伍拾贰万元整",
  "priceFormType": "固定总价",
  "components": [
    {
      "name": "公共租赁房部分监理酬金",
      "value": 7645300,
      "taxRate": "6%",
      "tax": null
    },
    {
      "name": "共有产权房部分监理酬金",
      "value": 2874700,
      "taxRate": "6%",
      "tax": null
    }
  ]
}

输出：
{
  "calculatedSum": 10520000,
  "isPriceConsistent": true,
  "priceInconsistencyDescription": "",
  "calculationDetails": {
    "validComponents": ["公共租赁房部分监理酬金", "共有产权房部分监理酬金"],
    "skippedComponents": [],
    "componentCount": 2
  }
}

**示例2：有分项但总和不一致**
输入：
{
  "contractPriceTotal": 10520000,
  "contractPriceTotalChinese": "壹仟零伍拾贰万元整",
  "priceFormType": "固定总价",
  "components": [
    {
      "name": "公共租赁房部分监理酬金",
      "value": 7645300,
      "taxRate": "6%",
      "tax": null
    },
    {
      "name": "共有产权房部分监理酬金",
      "value": 2800000,
      "taxRate": "6%",
      "tax": null
    }
  ]
}

输出：
{
  "calculatedSum": 10445300,
  "isPriceConsistent": false,
  "priceInconsistencyDescription": "签约酬金10520000元与分项合计10445300元不符，差额74700元",
  "calculationDetails": {
    "validComponents": ["公共租赁房部分监理酬金", "共有产权房部分监理酬金"],
    "skippedComponents": [],
    "componentCount": 2
  }
}

**示例3：无分项且一致**
输入：
{
  "contractPriceTotal": 10520000,
  "contractPriceTotalChinese": "壹仟零伍拾贰万元整",
  "priceFormType": "固定总价",
  "components": []
}

输出：
{
  "calculatedSum": 10520000,
  "isPriceConsistent": true,
  "priceInconsistencyDescription": "",
  "calculationDetails": {
    "validComponents": [],
    "skippedComponents": [],
    "componentCount": 0
  }
}

**示例4：监理酬金+相关服务酬金且一致**
输入：
{
  "contractPriceTotal": 10520000,
  "contractPriceTotalChinese": "壹仟零伍拾贰万元整",
  "priceFormType": "固定总价",
  "components": [
    {
      "name": "监理酬金",
      "value": 9000000,
      "taxRate": "6%",
      "tax": null
    },
    {
      "name": "相关服务酬金",
      "value": 1520000,
      "taxRate": "6%",
      "tax": null
    }
  ]
}

输出：
{
  "calculatedSum": 10520000,
  "isPriceConsistent": true,
  "priceInconsistencyDescription": "",
  "calculationDetails": {
    "validComponents": ["监理酬金", "相关服务酬金"],
    "skippedComponents": [],
    "componentCount": 2
  }
}

请立即验算并输出JSON。calculatedSum必须是纯数字！
"""







PROMPT_PART1_质量标准 = """
你是专业的合同质量管理专家。请从"质量标准"章节中提取质量要求。

**提取内容：**
1. 设计质量标准
2. 施工质量标准
3. 创优目标（如有）

**输出JSON格式：**
```json
{
  "qualityStandards": {
    "designQuality": "设计质量标准描述",
    "constructionQuality": "施工质量标准描述",
    "excellenceTarget": "创优目标（如：争创鲁班奖、钱江杯等），没有则填null"
  }
}
```

只输出JSON，不要任何解释。
"""



PROMPT_PART_3_REFINED = """
你是专业的合同分析专家。请从"第三部分 专用合同条件"中提取条款信息，重点识别明确的风险点。

**重点关注条款：**
1. 付款条件：是否存在明显不利条款（如季付改月付）
2. 违约责任：罚款标准是否过于严苛（如日罚万分之五以上）
3. 索赔程序：时限是否过短（如3天内提交）
4. 质保期：是否过长（超过行业标准）
5. 义务分配：是否明显失衡

**输出JSON格式：**
```json
{
  "clauses": {
    "scope": "承包范围完整描述",
    "obligations": {
      "employer": ["发包人具体义务1", "发包人具体义务2"],
      "contractor": ["承包人具体义务1", "承包人具体义务2"]
    },
    "claims": "变更索赔条款详细内容，包含具体时限要求",
    "rewards": "奖惩机制详细内容，包含具体标准",
    "disputes": "争议解决方式详细内容"
  },
  "documents": [
    {"name": "文档名称", "page": "页码数值"}
  ],
  "preliminaryRisks": [
    {
      "type": "付款风险/违约风险/索赔风险/质保风险/义务风险",
      "description": "具体风险描述，引用原文", 
      "clause": "相关条款位置",
      "severity": "高/中/低",
      "specificIssue": "具体问题，如：索赔通知时限仅3天，远低于行业惯例的28天"
    }
  ]
}
```

**重要提醒：**
1. 只标记有明确问题的条款为风险
2. 风险描述必须引用具体条款内容
3. 必须说明为什么是风险（对比行业标准）

只输出JSON，不要其他内容。
"""

# 新增第三部分专用合同条件的专用分析提示词
PROMPT_PART3_付款条件分析 = """
你是专业的合同财务条款分析专家。请从专用合同条件中提取和分析付款相关条款。

**分析重点：**
1. 付款进度和时间安排
2. 付款条件和前置要求
3. 逾期付款的处理
4. 预付款、进度款、结算款的安排
5. 保留金和质保金的规定

**提取任务：**
1. 识别付款相关的所有条款
2. 提取具体的付款时间、条件、金额
3. 分析付款条件是否合理和平衡
4. 识别可能的付款风险点

**输出JSON格式：**
```json
{
  "paymentClauses": {
    "advancePayment": {
      "hasAdvance": true/false,
      "percentage": "预付款比例（如10%）",
      "conditions": "预付款支付条件",
      "repaymentMethod": "预付款扣回方式"
    },
    "progressPayment": {
      "schedule": "进度款支付安排描述",
      "conditions": "进度款支付条件",
      "percentage": "每次支付比例"
    },
    "finalPayment": {
      "retentionPercentage": "保留金比例",
      "releaseConditions": "保留金释放条件",
      "finalSettlementTime": "最终结算时间要求"
    },
    "overduePayment": {
      "interestRate": "逾期付款利息率",
      "interestBasis": "计息基础"
    }
  },
  "paymentRisks": [
    {
      "riskType": "付款风险类型",
      "description": "具体风险描述",
      "severity": "高/中/低",
      "suggestion": "改进建议"
    }
  ]
}
```

只输出JSON，不要任何解释。
"""

PROMPT_PART3_违约责任分析 = """
你是专业的合同违约条款分析专家。请从专用合同条件中提取和分析违约责任相关条款。

**分析重点：**
1. 各类违约行为的定义和认定标准
2. 违约金的计算方法和标准
3. 违约责任的承担方式
4. 免责条款和免责条件
5. 违约责任的时限要求

**提取任务：**
1. 识别所有违约责任条款
2. 提取具体的违约标准和惩罚措施
3. 分析违约责任是否对等和合理
4. 识别过于严苛或不平衡的条款

**输出JSON格式：**
```json
{
  "breachClauses": {
    "timeRelatedBreaches": {
      "delayPenalty": {
        "rate": "误期违约金率（如万分之五/天）",
        "calculation": "计算方式",
        "cap": "是否有上限"
      },
      "definition": "工期延误的认定标准"
    },
    "qualityBreaches": {
      "qualityStandards": "质量违约的标准",
      "penaltyMethods": "质量违约的惩罚方式"
    },
    "paymentBreaches": {
      "latePaymentPenalty": "逾期付款违约金",
      "amountReduction": "是否可以减扣工程款"
    },
    "otherBreaches": [
      {
        "breachType": "违约类型",
        "definition": "认定标准",
        "penalty": "违约责任"
      }
    ]
  },
  "breachRisks": [
    {
      "riskType": "违约风险类型",
      "description": "具体风险描述",
      "severity": "高/中/低",
      "reason": "风险原因分析"
    }
  ]
}
```

只输出JSON，不要任何解释。
"""

PROMPT_PART3_索赔变更分析 = """
你是专业的合同变更和索赔条款分析专家。请从专用合同条件中提取和分析变更索赔相关条款。

**分析重点：**
1. 变更的定义、范围和程序
2. 索赔的提出时限和要求
3. 索赔证据和证明材料要求
4. 变更价款的确定方法
5. 争议解决机制

**提取任务：**
1. 识别所有变更索赔条款
2. 提取具体的程序、时限、要求
3. 分析变更索赔条款的合理性
4. 识别可能阻碍索赔的程序性障碍

**输出JSON格式：**
```json
{
  "variationAndClaimClauses": {
    "variationProcedures": {
      "initiation": "变更提出的程序和要求",
      "approval": "变更批准的程序和权限",
      "documentation": "变更的文档要求"
    },
    "claimProcedures": {
      "noticeTimeLimit": "索赔通知时限",
      "submissionTimeLimit": "索赔报告提交时限",
      "documentationRequirements": "索赔证据和文档要求"
    },
    "valuation": {
      "pricingMethod": "变更价款确定方法",
      "rateDetermination": "费率确定原则",
      "disputeResolution": "价格争议解决方式"
    }
  },
  "claimRisks": [
    {
      "riskType": "索赔风险类型",
      "description": "具体风险描述",
      "timeLimit": "相关时限要求",
      "severity": "高/中/低",
      "impact": "对承包商的影响"
    }
  ]
}
```

只输出JSON，不要任何解释。
"""

PROMPT_PART3_权利义务分析 = """
你是专业的合同权利义务分析专家。请从专用合同条件中提取和分析双方权利义务相关条款。

**分析重点：**
1. 发包人和承包人的具体义务
2. 权利和责任的对等性
3. 管理职责的分配
4. 协助义务的履行
5. 风险分担的合理性

**提取任务：**
1. 识别所有权利义务条款
2. 提取具体的义务内容和要求
3. 分析义务分配是否平衡合理
4. 识别可能存在的不公平条款

**输出JSON格式：**
```json
{
  "rightsAndObligations": {
    "employerObligations": [
      {
        "obligation": "发包人义务描述",
        "timeRequirement": "时间要求",
        "penaltyForNonCompliance": "不履行的后果"
      }
    ],
    "contractorObligations": [
      {
        "obligation": "承包人义务描述",
        "timeRequirement": "时间要求",
        "penaltyForNonCompliance": "不履行的后果"
      }
    ],
    "riskAllocation": {
      "technicalRisks": "技术风险分担",
      "financialRisks": "财务风险分担",
      "managementRisks": "管理风险分担"
    },
    "assistanceObligations": {
      "employerAssistance": "发包人协助义务",
      "contractorAssistance": "承包人协助义务"
    }
  },
  "balanceRisks": [
    {
      "riskType": "平衡性风险",
      "description": "具体描述",
      "severity": "高/中/低",
      "unfairness": "不公平的具体表现"
    }
  ]
}
```

只输出JSON，不要任何解释。
"""

PROMPT_PART3_争议解决分析 = """
你是专业的合同争议解决条款分析专家。请从专用合同条件中提取和分析争议解决相关条款。

**分析重点：**
1. 争议解决的方式和程序
2. 争议解决机构的选择
3. 争议解决的时限要求
4. 法律适用和管辖权
5. 争议期间的合同履行

**提取任务：**
1. 识别所有争议解决条款
2. 提取具体的解决程序和要求
3. 分析争议解决机制的有效性
4. 识别可能拖延或偏袒的条款

**输出JSON格式：```json
{
  "disputeResolution": {
    "resolutionMethods": [
      {
        "method": "争议解决方式（协商/调解/仲裁/诉讼）",
        "procedure": "具体程序和要求",
        "institution": "解决机构（如有）"
      }
    ],
    "arbitrationClause": {
      "institution": "仲裁机构",
      "rules": "仲裁规则",
      "seat": "仲裁地",
      "language": "仲裁语言"
    },
    "litigationClause": {
      "court": "管辖法院",
      "applicableLaw": "适用法律"
    },
    "interimMeasures": {
      "continuation": "争议期间合同是否继续履行",
      "escalation": "升级程序"
    }
  },
  "resolutionRisks": [
    {
      "riskType": "争议解决风险",
      "description": "具体风险描述",
      "severity": "高/中/低",
      "recommendation": "改进建议"
    }
  ]
}
```

只输出JSON，不要任何解释。
"""

PROMPT_COMPREHENSIVE_ANALYSIS_SIMPLIFIED = """
你是资深的合同分析专家。请基于提供的合同信息进行客观分析。

## 评分标准（二分法）

**价款或报酬：**
- 100分：价格计算准确，各项费用一致
- 扣分条件：价格不一致（扣20分）、计算错误（扣10-30分）、费用缺失（扣10分）

**履行期限：**
- 100分：工期与起止日期一致，安排合理
- 扣分条件：日期计算不符（扣20分）、工期明显不合理（扣10-30分）、表述问题如天和日历天不对应（扣5分）

**双方权利义务：**
- 100分：义务分配合理，无明显失衡
- 扣分条件：义务严重失衡（扣15-20分）、关键义务缺失（扣20分）

**变更与索赔：**
- 100分：程序合理，时限适当
- 扣分条件：时限过短（<7天扣11-15分，<3天扣20-30分）、程序过于复杂（扣5-10分）

**奖惩机制：**
- 100分：有奖有罚，标准合理
- 扣分条件：只罚不奖（扣5-10分）、罚款过重（扣5-10分）、标准不明（扣10-20分）

**其他项目（招标人、工程概况、项目背景、承包范围、合同文件构成、争议解决）：**
- 默认100分，除非信息严重缺失

## 输出要求
只输出assessment部分，格式如下：  如果100分，description写信息完整清晰，如果不是100分，简写扣分原因。
```json
{
    "assessment": [
        {"label": "招标人", "score": 100, "description": "信息完整清晰"},
        {"label": "工程概况", "score": 100, "description": "评分说明"},
        {"label": "项目背景", "score": 100, "description": "评分说明"},
        {"label": "承包范围", "score": 100, "description": "评分说明"},
        {"label": "价款或报酬", "score": 80, "description": "扣分原因"},
        {"label": "履行期限", "score": 100, "description": "评分说明"},
        {"label": "合同文件构成", "score": 100, "description": "评分说明"},
        {"label": "双方权利义务", "score": 70, "description": "扣分原因"},
        {"label": "争议解决", "score": 100, "description": "评分说明"},
        {"label": "变更与索赔", "score": 70, "description": "扣分原因"},
        {"label": "奖惩", "score": 70, "description": "扣分原因"}
    ]
}
```

**关键原则：**
1. 只有发现明确问题才扣分，模糊的"可能问题"不扣分
2. 所有风险必须基于具体条款，不得主观推测
3. 建议必须可操作，包含具体修改内容
4. 数值不加引号，空数组保留[]格式

只输出JSON，不要其他内容。
"""





CONTRACT_ONLY_PROMPT = """
你是专业的合同分析专家。请从提供的合同文本中，提取关键信息，并严格按照以下JSON格式输出。

```json
{
  "projectInfo": {
    "projectName": "项目全称",
    "projectLocation": "项目地点",
    "projectFundingSource": "项目资金来源",
    "page": 2
  },
  "parties": {
    "employer": "发包人名称",
    "contractorLead": "承包人（牵头方）",
    "contractorMember": "承包人（成员方）",
    "page": 2
  },
  "finance": {
    "contractPriceTotal": 793843000,
    "page": 4,
    "isPriceConsistent": false,
    "priceInconsistencyDescription": "合同总价与分项合计不符的具体描述",
    "components": [
      {"name": "设计费", "value": 7341400},
      {"name": "建筑安装工程费", "value": 727914900},
      {"name": "暂列金额", "value": 50090500}
    ]
  },
  "duration": {
    "totalDurationDays": 970,
    "plannedStartDate": "YYYY-MM-DD",
    "plannedCompletionDate": "YYYY-MM-DD",
    "page": 3,
    "isDurationConsistent": false,
    "durationInconsistencyDescription": "工期与计划日期不符的具体描述",
    "projectMilestones": [
      {
        "name": "里程碑名称",
        "timePoint": "时间点描述",
        "description": "里程碑具体描述"
      }
    ]
  },
  "qualityStandards": {
    "designQuality": "设计质量标准",
    "constructionQuality": "施工质量标准",
    "excellenceTarget": "工程创优目标",
    "page": 3
  },
  "clauses": {
    "scope": "承包范围描述",
    "obligations": {
      "employer": ["发包人义务1", "发包人义务2"],
      "contractor": ["承包人义务1", "承包人义务2"]
    },
    "claims": "变更索赔条款",
    "rewards": "奖惩机制",
    "disputes": "争议解决方式"
  },
  "documents": [
    {"name": "文档名称", "page": 2}
  ],
  "assessment": [
    {"label": "招标人", "score": 100, "description": "信息完整清晰。"},
    {"label": "工程概况", "score": 100, "description": "信息完整清晰。"},
    {"label": "项目背景", "score": 100, "description": "信息完整清晰。"},
    {"label": "承包范围", "score": 100, "description": "信息完整清晰。"},
    {"label": "价款或报酬", "score": 80, "description": "总价与分项合计不符。"},
    {"label": "履行期限", "score": 80, "description": "计划日期与总工期不符。"},
    {"label": "合同文件构成", "score": 100, "description": "信息完整清晰。"},
    {"label": "双方权利义务", "score": 100, "description": "信息完整清晰。"},
    {"label": "争议解决", "score": 100, "description": "信息完整清晰。"},
    {"label": "变更与索赔", "score": 100, "description": "信息完整清晰。"},
    {"label": "奖惩", "score": 100, "description": "信息完整清晰。"}
  ],
  "contractType": "epc",
  "templateType": "contract_only"
}
```

## 严格评分标准：

**评分标准（0-100分）：**

### 信息完整性评分：
- **90-100分**：信息完整、具体、清晰，包含所有必要细节
- **75-89分**：信息基本完整，有少量细节缺失但不影响理解
- **60-74分**：信息存在但不够完整，缺失重要细节或表述模糊
- **40-59分**：信息严重不足，仅有框架性描述或大量关键信息缺失
- **20-39分**：信息极少，仅有零星相关内容
- **0-19分**：完全缺失相关信息

### 特殊评分规则：
1. **"按通用条款执行"类表述**：最高不超过50分（表明缺乏具体约定）
2. **"按相关规定办理"类表述**：最高不超过45分
3. **仅列举无具体内容**：最高不超过60分
4. **关键数值信息（金额、日期、工期）完全缺失**：不超过20分

### 各项目具体要求：
- **项目背景**：需包含项目性质、建设必要性、投资背景等，仅有项目名称不超过30分
- **价款或报酬**：必须有明确总价和主要分项，缺失总价不超过20分
- **履行期限**：必须有具体开工日期、竣工日期和总工期，缺失任一项扣20分
- **承包范围**：需详细描述具体工程内容，仅有"按工程量清单"不超过60分
- **奖惩机制**：仅有处罚无奖励机制不超过60分，完全缺失不超过30分

## 关键要求：
1. 严格按照上述JSON结构输出，不要增删字段
2. `assessment`必须是包含`label`, `score`, `description`对象的数组
3. **评分必须严格遵循上述标准，不得因"部分信息存在"而给予过高评分**
4. description字段必须客观描述信息的具体缺失情况和程度
5. 所有数值字段必须是数字，不能是字符串
6. 即使某些字段找不到，也要保留该字段并使用默认值


只输出JSON，不要其他内容。
"""












CONTRACT_WITH_TENDER_PROMPT = """
你是专业的合同与招标文件对比分析专家。请基于提供的`contractAnalysis`（合同分析结果）和`tenderAnalysis`（招标文件分析结果）JSON数据，进行全面、深入的对比分析，并严格按照下面指定的JSON格式输出最终的综合报告。

**输出JSON模板:**
```json
{
    "contract_id": "从输入数据中提取或生成一个唯一ID",
    "analysis_date": "生成当前日期和时间 (YYYY-MM-DD HH:MM:SS)",
    "templateType": "contract_with_tender",
    "projectInfo": {
        "projectName": "使用合同中的项目名称",
        "projectLocation": "使用合同中的项目地点",
        "projectArea": "提取或估算项目面积",
        "isProjectInfoConsistent": "对比项目名称、地点等信息后判断 (true/false)",
        "projectInfoDeviation": "如果不一致，在此详细说明偏差"
    },
    "parties": {
        "employer": "使用合同中的发包人名称",
        "contractorLead": "使用合同中的承包人牵头方",
        "contractorMember": "使用合同中的承包人成员方",
        "isPartiesConsistent": "对比发包人、承包人信息后判断 (true/false)",
        "partiesDeviation": "如果不一致，在此详细说明偏差"
    },
    "finance": {
        "contractPriceTotal": "使用合同中的总价 (数字)",
        "isPriceConsistent": "使用合同中的价格一致性判断 (true/false)",
        "priceInconsistencyDescription": "使用合同中的价格不一致描述"
    },
    "duration": {
        "totalDurationDays": "使用合同中的总工期 (数字)",
        "plannedStartDate": "使用合同中的计划开始日期",
        "plannedCompletionDate": "使用合同中的计划完成日期",
        "isDurationConsistent": "使用合同中的工期一致性判断 (true/false)",
        "durationInconsistencyDescription": "使用合同中的工期不一致描述"
    },
    "clauses": "{直接从contractAnalysis中复制clauses对象}",
    "assessment": "{直接从contractAnalysis中复制assessment数组}",
    "tenderCompliance": {
        "labels": ["项目基础信息符合性", "工期进度符合性", "质量标准符合性", "付款条件符合性", "担保保险符合性", "权责义务符合性", "风险责任符合性", "争议解决符合性"],
        "scores": "[根据对比分析，为每个label生成一个0-100的分数]"
    },
    "riskSummary": {
        "highRisk": "统计高风险项数量 (数字)",
        "mediumRisk": "统计中风险项数量 (数字)",
        "lowRisk": "统计低风险项数量 (数字)"
    },
    "complianceRate": "根据tenderCompliance的平均分计算整体符合率 (数字)",
    "priceDeviation": "详细描述合同总价与招标控制价的偏差率和分析",
    "durationDeviation": "详细描述合同工期与招标要求的差异及关键节点偏差",
    "technicalComparison": [
        {
            "category": "技术要求的类别，如'设计标准'",
            "tenderRequirement": "招标文件的具体要求",
            "contractClause": "合同中的对应条款",
            "compliance": "符合/偏离/轻微偏离",
            "riskLevel": "高/中/低"
        }
    ],
    "commercialComparison": [
        {
            "category": "商务条件的类别，如'付款条件'",
            "tenderRequirement": "招标文件的具体要求",
            "contractClause": "合同中的对应条款",
            "compliance": "符合/偏离",
            "impact": "该偏差对承包商的具体影响分析"
        }
    ],
    "managementComparison": [
        {
            "area": "管理领域，如'项目经理要求'",
            "tenderRequirement": "招标文件的具体要求",
            "contractClause": "合同中的对应条款",
            "consistency": "一致/不一致/基本一致"
        }
    ],
    "legalComparison": [
        {
            "clause": "法律条款，如'违约责任'",
            "tenderClause": "招标文件的具体条款",
            "contractClause": "合同中的对应条款",
            "difference": "详细说明两者差异"
        }
    ],
    "highRisks": [
        {
            "title": "高风险项的标题",
            "description": "详细描述风险内容",
            "impact": "该风险可能造成的影响",
            "timeline": "建议处理该风险的时间点",
            "category": "风险分类 (财务/管理/法律/技术)"
        }
    ],
    "mediumRisks": [
        {
            "title": "中风险项的标题",
            "description": "详细描述风险内容",
            "suggestion": "针对该风险的具体修改或应对建议",
            "category": "风险分类"
        }
    ],
    "lowRisks": [
        {
            "title": "低风险项的标题",
            "description": "详细描述风险内容",
            "category": "风险分类"
        }
    ],
    "immediateActions": [
        {
            "action": "需要立即执行的行动项",
            "description": "行动项的具体内容",
            "deadline": "完成时限 (如'签约前')",
            "responsible": "负责部门或团队"
        }
    ],
    "mediumTermSuggestions": [
        {
            "suggestion": "中期建议",
            "description": "建议的具体内容",
            "timeline": "建议执行的时间范围",
            "priority": "高/中/低"
        }
    ],
    "longTermOptimizations": [
        {
            "optimization": "长期优化建议",
            "description": "建议的具体内容",
            "expectedBenefit": "预期收益",
            "department": "负责部门"
        }
    ],
    "contractType": "从输入数据中提取合同类型"
}
```

**关键指令:**
1.  **数据来源**: 你的唯一信息来源是输入的`analysis_results_json`，它包含`contractAnalysis`和`tenderAnalysis`两部分。
2.  **结构严格**: 必须严格遵守上述JSON模板，不得增删或修改顶级字段。
3.  **内容填充**:
    - 对于明确指示为`{直接从...复制}`的字段，请直接复制对应的数据块。
    - 对于需要对比分析的字段（如`isProjectInfoConsistent`, `technicalComparison`等），请基于输入数据进行逻辑判断和信息提取。
    - 对于需要生成的字段（如`analysis_date`, `scores`, `complianceRate`等），请根据指令进行计算或生成。
4.  **数值格式**: 所有表示金额、数量、天数、百分比、得分的字段，其值必须是**数字(Number)**，而不是字符串。
5.  **空值处理**: 如果某个字段在源数据中找不到对应内容，请使用合理的默认值（例如，字符串用`""`，数组用`[]`，对象用`{}`）。

现在，请开始分析并生成最终的综合报告。
"""





#通用合同识别
GENERIC_CONTRACT_PROMPT = """
你是专业的合同分析专家。请从提供的合同文本中，提取关键信息，并做检查
**金额检查重点：**
1. 合同总价是否等于各分项费用之和
2. 设计费+建安费+暂列金额是否等于合同总价  
3. 数字与大写金额是否一致
4. 是否存在计算错误或遗漏项

**时间检查重点：**
1. 按起止日期计算的实际天数是否与总工期一致
2. 工期单位是否统一（日历天/工作日）
3. 里程碑时间安排是否合理
4. 是否存在时间逻辑错误

**检查方法：**
- 金额：将所有分项费用相加，与合同总价对比
- 时间：用结束日期减去开始日期，与总工期对比

结果严格按照以下JSON格式输出。
```json
{
  "projectInfo": {
    "projectName": "项目全称",
    "projectLocation": "项目地点（可选）",
    "projectFundingSource": "项目资金来源（可选）",
    "page": 页码数字
  },
  "parties": {
    "employer": "发包人/甲方名称",
    "contractorLead": "承包人/乙方名称",
    "contractorMember": "承包人成员方（可选）",
    "page": 页码数字
  },
  "finance": {
    "contractPriceTotal": "合同总价数值",
    "contractPriceTotalChinese": "合同总价大写（可选）",
    "page": "页码数字",
    "isPriceConsistent": "true或false",
    "priceInconsistencyDescription": "价格不一致的具体描述（仅当isPriceConsistent为false时）",
    "components": [
      {"name": "识别出的费用项名称1", "value": "金额数值1", "chinese": "大写金额1（可选）"},
      {"name": "识别出的费用项名称2", "value": "金额数值2", "chinese": "大写金额2（可选）"}
    ]
  },
  "duration": {
    "totalDurationDays": 总工期天数（可选）,
    "plannedStartDate": "YYYY-MM-DD格式开始日期（可选）",
    "plannedCompletionDate": "YYYY-MM-DD格式完成日期（可选）",
    "page": 页码数字,
    "isDurationConsistent": true或false,
    "durationInconsistencyDescription": "工期不一致的具体描述（仅当isDurationConsistent为false时）",
    "projectMilestones": [
      {
        "name": "里程碑名称",
        "timePoint": "时间点描述",
        "description": "里程碑具体描述"
      }
    ]
  },
  "qualityStandards": {
    "designQuality": "设计质量标准（可选）",
    "constructionQuality": "施工质量标准（可选）",
    "serviceQuality": "服务质量标准（可选）",
    "excellenceTarget": "工程创优目标（可选）",
    "page": 页码数字
  },
  "clauses": {
    "scope": "承包范围/服务内容描述（仅当合同中明确提及时包含）",
    "obligations": {
      "employer": ["发包人义务1", "发包人义务2"],
      "contractor": ["承包人义务1", "承包人义务2"]
    },
    "disputes": "争议解决方式（仅当合同中明确提及时包含）",
    "confidentiality": "保密要求条款（仅当合同中明确提及时包含）",
    "claims": "变更索赔条款（仅当合同中明确提及时包含）",
    "rewards": "奖惩机制（仅当合同中明确提及时包含）",
    "quality": "质量标准要求（仅当合同中明确提及时包含）",
    "payment": "付款条件详细描述（仅当合同中明确提及时包含）",
    "liability": "责任划分条款（仅当合同中明确提及时包含）",
    "termination": "合同终止条件（仅当合同中明确提及时包含）"
  },
  "documents": [
    {"name": "文档名称1", "page": 页码数字},
    {"name": "文档名称2", "page": 页码数字}
  ],
  "assessment": [
    {"label": "基本信息", "score": 95, "description": "具体评价描述"},
    {"label": "参与方信息", "score": 90, "description": "具体评价描述"},
    {"label": "价款条款", "score": 85, "description": "具体评价描述"},
    {"label": "履行条件", "score": 80, "description": "具体评价描述"},
    {"label": "权责划分", "score": 95, "description": "具体评价描述"}
  ],
  "contractType": "generic",
  "templateType": "contract_only"
}
只输出JSON，不要其他内容。
"""





# 招标文件与合同对比分析API提示词

CONTRACT_and_TENDER_PROMPT_1 = """
你是一位专业的合同分析专家，需要对比分析投标人须知前附表的招标要求与实际签署合同的差异，识别所有偏差点并评估符合性。

** 输入数据 **
1. **投标人须知前附表内容**：包含招标要求的详细条款
2. **合同JSON数据**：包含已签署合同的具体内容

## 输出要求
请严格按照以下JSON格式输出对比分析结果，所有字段都必须填写：

```json
{
    "projectInfoComparison": {
        "projectName": {
            "tenderRequirement": "招标文件中的工程名称",
            "contractClause": "合同中的工程名称", 
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        },
        "projectLocation": {
            "tenderRequirement": "招标文件中的建设地点",
            "contractClause": "合同中的建设地点",
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        },
        "fundingSource": {
            "tenderRequirement": "招标文件中的资金来源",
            "contractClause": "合同中的资金来源",
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        }
    },
    
    "partiesComparison": {
        "employer": {
            "tenderRequirement": "招标文件中的招标人名称",
            "contractClause": "合同中的发包人名称",
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        },
        "contractorRequirement": {
            "tenderRequirement": "招标文件对承包人的要求（联合体等）",
            "contractClause": "合同中实际的承包人构成",
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        }
    },
    
    "financeComparison": {
        "totalPrice": {
            "tenderMaxPrice": 招标文件最高投标限价（数字），
            "riskControlPrice": 招标文件风险控制价（数字），
            "contractPrice": 合同总价（数字），
            "deviationRate": 合同价格偏离招标限价的百分比（数字），
            "isWithinLimit": true/false,
            "analysis": "价格对比分析说明"
        },
        "designFee": {
            "tenderLimit": 招标文件设计费限价（数字），
            "contractAmount": 合同设计费（数字），
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        },
        "constructionFee": {
            "tenderLimit": 招标文件建安费限价（数字），
            "contractAmount": 合同建安费（数字），
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        }
    },
    
    "durationComparison": {
        "totalDuration": {
            "tenderRequirement": 招标要求总工期天数（数字），
            "contractClause": 合同约定总工期天数（数字），
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        },
        "keyMilestones": {
            "designCompletion": {
                "tenderRequirement": "招标文件要求的设计完成时间",
                "contractClause": "合同约定的设计完成时间",
                "isConsistent": true/false,
                "deviation": "具体偏差描述，无偏差时为空字符串"
            },
            "constructionMilestones": {
                "tenderRequirement": "招标文件要求的施工关键节点",
                "contractClause": "合同约定的施工关键节点",
                "isConsistent": true/false,
                "deviation": "具体偏差描述，无偏差时为空字符串"
            }
        }
    },
    
    "qualityComparison": {
        "designQuality": {
            "tenderRequirement": "招标文件的设计质量标准",
            "contractClause": "合同约定的设计质量标准",
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        },
        "constructionQuality": {
            "tenderRequirement": "招标文件的施工质量标准",
            "contractClause": "合同约定的施工质量标准", 
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        }
    },
    
    "scopeComparison": {
        "contractScope": {
            "tenderRequirement": "招标文件的承包范围要求",
            "contractClause": "合同约定的承包范围",
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        }
    },
    
    "commercialComparison": {
        "tenderBond": {
            "tenderRequirement": "招标文件要求的投标担保",
            "contractClause": "合同中相关担保条款",
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        },
        "performanceBond": {
            "tenderRequirement": "招标文件要求的履约担保",
            "contractClause": "合同约定的履约担保",
            "isConsistent": true/false,
            "deviation": "具体偏差描述，无偏差时为空字符串"
        }
    },
    
    "overallAssessment": {
        "complianceRate": 整体符合率百分比（数字），
        "majorDeviations": [
            "重大偏差1",
            "重大偏差2"
        ],
        "riskLevel": "高/中/低",
        "summary": "整体对比分析总结"
    }
}
```

## 对比分析重点关注

### 1. 数值精度对比
- 价格金额要精确到元
- 工期天数要准确
- 百分比保留一位小数

### 2. 条款文字对比
- 关注表述的完整性
- 识别关键词差异
- 注意条件限制的变化

### 3. 偏差程度评估
- **完全一致**：条款内容100%匹配
- **基本一致**：核心内容相同，表述略有差异
- **轻微偏离**：有小幅改变但不影响核心要求
- **重大偏离**：关键条件发生重要变化
- **完全不符**：与招标要求完全不同

### 4. 风险识别原则
- **高风险**：影响合同履行或项目成功的重大偏差
- **中风险**：可能引起争议或增加成本的偏差  
- **低风险**：对项目影响较小的细微差异

## 分析注意事项

1. **务必基于实际内容**：严格按照提供的招标文件和合同内容进行对比，不要添加假设信息
2. **保持客观中性**：如实反映差异，不带主观倾向性评价
3. **量化分析优先**：能量化的数据尽量给出具体数字和比例
4. **突出关键差异**：重点标识可能影响项目履行的重要偏差
5. **格式严格遵守**：输出的JSON必须格式正确，字段完整

请开始分析并输出完整的对比结果。
只返回json
"""







PROMPT_TENDER_INITIAL_ANALYSIS = """
你是专业的招标文件分析专家。请根据招标文件的标题和开头部分内容，快速判断其类型并提取项目名称。

**招标文件类型识别规则:**
- **施工招标**: 主要内容为工程施工，如土建、安装等。
- **EPC招标**: 包含设计(Design)、采购(Procurement)、施工(Construction)全过程。
- **设计招标**: 仅涉及项目的设计服务。
- **监理招标**: 仅涉及项目的监理服务。
- **设备采购招标**: 主要为设备或材料的采购。
- **服务招标**: 如咨询、勘察等服务。
- **通用未知**: 如果无法明确判断，则使用此类型。

**输出要求:**
- 只输出JSON格式。
- JSON中必须包含 `tenderType` 和 `projectInfo` 字段。
- `tenderType` 的可能值包括: "施工招标", "EPC招标", "设计招标", "监理招标", "设备采购招标", "服务招标", "通用未知"。

**示例:**
```json
{
  "tenderType": "施工招标",
  "projectInfo": {
    "projectName": "项目全称（如果能快速找到）"
  }
}
```
请开始分析以下招标文件内容：
"""

PROMPT_PROJECT_MATCHING = """
你是项目匹配验证专家。请基于以下从合同和招标文件中分别提取的初步信息，判断它们是否描述的是同一个项目。

**判断依据:**
1.  **项目名称**: 是否高度相似、包含或被包含。
2.  **核心关键词**: 是否共享项目地点、业主单位、工程性质等关键词。
3.  **常识判断**: 结合项目名称的通用结构进行判断。

**输入信息:**
- **合同信息**: {contract_info_json}
- **招标文件信息**: {tender_info_json}

**输出要求:**
- 严格按照以下JSON格式输出。
- `isMatch` 必须是布尔值 (true/false)。
- `matchConfidence` 必须是 "high", "medium", "low"之一。
- `reason` 字段必须清晰地解释你的判断逻辑。

**示例:**
```json
{
  "isMatch": true,
  "matchConfidence": "high",
  "reason": "项目名称完全一致。"
}
```

或者

```json
{
  "isMatch": false,
  "matchConfidence": "high",
  "reason": "项目名称'A项目'和'B项目'完全不同，且无共享关键词。"
}
```
请开始分析。
"""

# --- Tender Document Section Prompts ---

PROMPT_TENDER_CHAPTER_1 = """
你是专业的招标采购专家。请从"第一章 招标公告"中提取核心项目信息。

**输出JSON格式:**
```json
{
  "projectOverview": {
    "projectName": "项目全称",
    "projectCode": "项目编码（如有）",
    "projectLocation": "项目地点",
    "projectOwner": "招标人/项目业主",
    "tenderAgent": "招标代理机构（如有）",
    "projectDescription": "项目概况、规模和内容"
  },
  "bidderRequirements": {
    "qualification": ["投标人主要资格要求1", "投标人主要资格要求2"],
    "financialStanding": "财务能力要求（如注册资本、近年营收等）",
    "pastPerformance": "类似项目业绩要求"
  },
  "timeline": {
    "documentAcquisition": "获取招标文件的时间和方式",
    "submissionDeadline": "投标文件递交的截止时间",
    "bidOpeningTime": "开标时间"
  }
}
```
只输出JSON，不要其他内容。
"""

PROMPT_TENDER_CHAPTER_2 = """
你是专业的招标采购专家。请从"第二章 投标人须知"中提取关键的商务和程序性条款。

**输出JSON格式:**
```json
{
  "submissionRequirements": {
    "fileComposition": "投标文件的组成（商务、技术、报价等部分）",
    "sealingAndMarking": "投标文件的密封和标记要求",
    "numberOfCopies": "需要提交的正副本数量"
  },
  "bidBond": {
    "amount": "投标保证金的金额",
    "form": "保证金形式（如电汇、保函）",
    "submissionRequirement": "提交要求和截止时间"
  },
  "validityPeriod": {
    "duration": "投标有效期（天数）",
    "extensionClause": "是否允许延长及其条件"
  },
  "riskAllocation": [
    {
      "riskType": "风险类型（如踏勘现场、报价风险等）",
      "description": "相关条款的原文描述"
    }
  ]
}
```
只输出JSON，不要其他内容。
"""

PROMPT_TENDER_CHAPTER_3 = """
你是专业的评标专家。请从"第三章 评标办法"中提取详细的评估标准和流程。

**输出JSON格式:**
```json
{
  "evaluationMethod": "评标方法（如综合评估法、经评审的最低投标价法）",
  "preliminaryReview": {
    "criteria": ["初步评审标准1（如资格审查、格式审查）", "初步评审标准2"]
  },
  "detailedReview": {
    "technicalScore": {
      "totalPoints": "技术部分总分",
      "scoringItems": [
        {"item": "评分项1（如施工方案）", "points": "分值"},
        {"item": "评分项2（如项目团队）", "points": "分值"}
      ]
    },
    "commercialScore": {
      "totalPoints": "商务部分总分",
      "priceCalculationMethod": "投标报价的计算和评审方法"
    }
  },
  "finalDecision": {
    "recommendationRule": "推荐中标候选人的规则",
    "tieBreakingMethod": "得分相同时的处理方法"
  }
}
```
只输出JSON，不要其他内容。
"""

PROMPT_TENDER_CHAPTER_5 = """
你是专业的技术和工程专家。请从"第五章 发包人要求"中提取关键的技术标准、规格和要求。

**输出JSON格式:**
```json
{
  "technicalStandards": [
    {"standardName": "采用的主要技术标准名称1", "details": "相关要求的简要描述"},
    {"standardName": "采用的主要技术标准名称2", "details": "相关要求的简要描述"}
  ],
  "keySpecifications": [
    {"item": "关键设备/材料1", "spec": "规格、型号、性能参数要求"},
    {"item": "关键设备/材料2", "spec": "规格、型号、性能参数要求"}
  ],
  "scopeOfWork": {
    "supplyScope": "供货范围",
    "serviceScope": "服务范围（如安装、调试、培训等）"
  },
  "qualityAndInspection": {
    "qualityRequirements": "质量要求和验收标准",
    "inspectionAndTesting": "检验和测试要求"
  }
}
```
只输出JSON，不要其他内容。
"""

# --- tender Document Sub-Chapter Prompts ---

PROMPT_TENDER_SUBCHAPTER_2_PREFACE = """
你是专业的招标采购专家。请从"投标人须知前附表"中，以表格形式提取所有关键数据点。

**输出JSON格式:**
```json
{
  "prefaceTable": [
    {"item": "提取到的条款号和名称1", "content": "对应的内容和规定1"},
    {"item": "提取到的条款号和名称2", "content": "对应的内容和规定2"}
  ]
}
```
只输出JSON，不要其他内容。确保将前附表中的每一项都作为一个独立的对象提取出来。
"""

PROMPT_TENDER_SUBCHAPTER_2_INSTRUCTIONS = """
你是专业的招标采购专家。请从"投标人须知"（正文部分）中，提取关键的程序性和要求条款。

**输出JSON格式:**
```json
{
  "generalProvisions": {
    "projectOverview": "项目概况和资金来源",
    "tenderScope": "招标范围",
    "bidderQualification": "投标人资格要求"
  },
  "tenderDocuments": {
    "composition": "招标文件的构成",
    "clarificationAndModification": "招标文件的澄清和修改程序"
  },
  "bidPreparation": {
    "languageAndCurrency": "投标语言、计量单位和货币",
    "bidPricing": "投标报价的要求",
    "alternativeBids": "是否接受备选投标方案"
  },
  "bidSubmission": {
    "deadline": "投标截止时间",
    "lateBids": "迟交投标文件的处理",
    "modificationAndWithdrawal": "投标的修改与撤回程序"
  }
}
```
只输出JSON，不要其他内容。
"""

# ==================== 中标通知书分析相关 Prompt ====================

PROMPT_AWARD_INITIAL_ANALYSIS = """
你是专业的建设工程文档分析专家。请从中标通知书的开头部分，快速提取基本信息用于项目匹配验证。

**输出要求:**
- 只输出JSON格式
- 提取项目名称和招标人信息

**示例:**
```json
{
  "documentType": "中标通知书",
  "projectInfo": {
    "projectName": "智造谷产业服务综合体项目（一期、二期）EPC工程总承包"
  },
  "employer": "杭州高新智造谷开发运营有限公司"
}
```
请开始分析以下中标通知书内容：
"""

PROMPT_AWARD_EXTRACTION = """
你是专业的建设工程文档分析专家。请从中标通知书中提取完整的结构化信息。

中标通知书通常包含：标题、发文日期、收件人（中标单位）、项目信息表格、中标范围说明等。

**输出JSON格式:**
```json
{
  "documentTitle": "杭州市建设工程EPC总承包中标通知书",
  "awardDate": "2021年08月31日",
  "tenderNumber": "11131120210723011",
  "projectName": "智造谷产业服务综合体项目（一期、二期）EPC工程总承包",
  "employer": "招标人名称",
  "winners": ["中标人1", "中标人2", "中标人3"],
  "awardPrice": 4156799100,
  "awardPriceUnit": "元",
  "awardPriceChinese": "肆拾壹亿伍仟陆佰柒拾玖万玖仟壹佰元",
  "duration": 790,
  "durationUnit": "日历天",
  "projectManager": "项目负责人姓名",
  "designManager": "设计负责人姓名",
  "constructionManager": "施工负责人（项目经理）姓名",
  "location": "建设地址详细描述",
  "totalArea": 568419.91,
  "areaUnit": "m²",
  "areaPhase1": 496255.77,
  "areaPhase2": 72164.14,
  "contractDeadline": "2021年9月30日",
  "scope": ["设计", "采购", "施工", "总承包管理"],
  "scopeDescription": "中标范围的详细描述"
}
```

**注意:**
1. 金额统一转换为元（不是万元）
2. 所有数值字段使用数字类型
3. 如果某字段找不到，使用null
4. 中标人可能是联合体，需要列出所有成员

只输出JSON，不要其他内容。
"""

PROMPT_AWARD_EXTRACTION_DESIGN = """
你是专业的建设工程文档分析专家。请从设计类中标通知书中提取完整的结构化信息。

**设计类中标通知书特点：**
- 标题包含"设计中标通知书"或类似表述
- 包含"总投资额"、"工程计费额"、"设计费"等字段
- 包含"设计服务范围"（如方案设计、初设、施工图等）
- 包含"设计周期"要求（而非施工工期）

**输出JSON格式:**
```json
{
  "documentTitle": "杭州市建设工程设计中标通知书",
  "awardDate": "2022年09月08日",
  "tenderNumber": "A330108012050263000121",
  "projectName": "江南路口小学（西侧地块）改造一期工程设计",
  "employer": "招标人名称",
  "winners": ["设计单位1", "设计单位2"],
  "totalInvestment": 985290000,
  "totalInvestmentUnit": "元",
  "totalInvestmentChinese": "玖亿捌仟伍佰贰拾玖万元",
  "calculationBasis": "总建筑面积109177.15m²（其中第一期约47013.95m²，第二期约62163.2m²）",
  "awardPrice": 63480000,
  "awardPriceUnit": "元",
  "awardPriceChinese": "陆仟叁佰肆拾捌万元",
  "designScope": ["方案设计", "初步设计", "施工图设计", "BIM设计"],
  "designScopeDescription": "包含主体建筑设计、水电设计、暖通设计、智能化设计、景观设计等全专业设计服务",
  "designDuration": "收到主管部门批复后20日历天，施工图设计40日历天",
  "projectManager": "设计负责人姓名",
  "location": "建设地址详细描述",
  "totalArea": 109177.15,
  "areaUnit": "m²",
  "areaPhase1": 47013.95,
  "areaPhase2": 62163.2,
  "contractDeadline": "2022年9月30日"
}
```

**字段说明:**
1. `totalInvestment`: 总投资额（整个工程的投资，单位：元）
2. `calculationBasis`: 工程计费额（用于计算设计费的依据，通常是建筑面积或造价）
3. `awardPrice`: 设计费（中标的设计服务费，单位：元）
4. `designScope`: 设计服务范围数组（如["方案设计", "初步设计", "施工图设计"]）
5. `designScopeDescription`: 设计范围详细描述
6. `designDuration`: 设计周期描述（文本格式，如"方案设计20日，施工图40日"）
7. `projectManager`: 设计负责人（对应合同中的设计项目负责人）

**注意:**
1. 所有金额统一转换为元（不是万元）
2. 所有数值字段使用数字类型
3. 如果某字段找不到，使用null
4. 设计单位可能是联合体，需要列出所有成员
5. `designDuration`是文本描述，不是单一数值

只输出JSON，不要其他内容。
"""

PROMPT_TENDER_COVER_EXTRACTION = """
你是专业的招标文件分析专家。请从招标文件的封面和前言部分（投标人须知前附表之前的内容）提取基本信息。

这部分内容通常包含：
- 招标文件标题
- 招标编号
- 招标人名称
- 招标代理机构
- 发布日期

**输出JSON格式:**
```json
{
  "documentTitle": "智造谷产业服务综合体项目（一期、二期）EPC工程总承包招标文件",
  "tenderNumber": "11131120210723011",
  "employer": "杭州高新智造谷开发运营有限公司",
  "tenderAgent": "杭州信达投资咨询估价监理有限公司",
  "publishDate": "2021-07-27",
  "tenderType": "EPC工程总承包",
  "qualificationReview": "资格后审"
}
```

只输出JSON，不要其他内容。
"""
