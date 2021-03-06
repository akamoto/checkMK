# yapf: disable
checkname = 'azure_sites'

info = [
    ['Resource'],
    [
        '{"kind": "functionapp", "group": "cldazspo-solutions-rg", "name": "spo-solutions-fa1", "tags": {"OpLevel": "Operation", "OpHours": "7x24", "CostCenter": "0000252980", "ITProduct": "C89 Collaboration Platform"}, "provider": "Microsoft.Web", "subscription": "e95edb66-81e8-4acd-9ae8-68623f1bf7e6", "type": "Microsoft.Web/sites", "id": "/subscriptions/e95edb66-81e8-4acd-9ae8-68623f1bf7e6/resourceGroups/cldazspo-solutions-rg/providers/Microsoft.Web/sites/spo-solutions-fa1", "identity": {"tenant_id": "e7b94e3c-1ad5-477d-be83-17106c6c8301", "principal_id": "15c0b993-4efa-4cc1-9880-d68c0f59ed42", "type": "SystemAssigned"}, "location": "westeurope"}'
    ], ['metrics following', '24'],
    ['name', 'aggregation', 'value', 'unit', 'timestamp', 'timegrain', 'filters'],
    ['TotalAppDomainsUnloaded', 'average', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Gen0Collections', 'average', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Gen1Collections', 'average', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Gen2Collections', 'average', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['BytesReceived', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None'],
    ['BytesSent', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None'],
    ['Http5xx', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['MemoryWorkingSet', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None'],
    ['AverageMemoryWorkingSet', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None'],
    ['FunctionExecutionUnits', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['FunctionExecutionCount', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['AppConnections', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Handles', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Threads', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['PrivateBytes', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None'],
    ['IoReadBytesPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M', 'None'],
    ['IoWriteBytesPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M', 'None'],
    ['IoOtherBytesPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M', 'None'],
    ['IoReadOperationsPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M', 'None'],
    [
        'IoWriteOperationsPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M',
        'None'
    ],
    [
        'IoOtherOperationsPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M',
        'None'
    ], ['RequestsInApplicationQueue', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['CurrentAssemblies', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['TotalAppDomains', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'], ['Resource'],
    [
        '{"kind": "app", "group": "cldazpaaswebapp06-rg", "location": "southeastasia", "tags": {"OpLevel": "Operation", "OpHours": "7x24", "CostCenter": "0000252980", "ITProduct": "CUV130_MS_IIS (Internet Information Server) Standard"}, "provider": "Microsoft.Web", "subscription": "e95edb66-81e8-4acd-9ae8-68623f1bf7e6", "type": "Microsoft.Web/sites", "id": "/subscriptions/e95edb66-81e8-4acd-9ae8-68623f1bf7e6/resourceGroups/cldazpaaswebapp06-rg/providers/Microsoft.Web/sites/zcldazwamonseas-as", "name": "zcldazwamonseas-as"}'
    ], ['metrics following', '33'],
    ['name', 'aggregation', 'value', 'unit', 'timestamp', 'timegrain', 'filters'],
    ['IoReadBytesPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M', 'None'],
    ['IoWriteBytesPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M', 'None'],
    ['IoOtherBytesPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M', 'None'],
    ['IoReadOperationsPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M', 'None'],
    [
        'IoWriteOperationsPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M',
        'None'
    ],
    [
        'IoOtherOperationsPerSecond', 'total', '0.0', 'bytes_per_second', '1536073080', 'PT1M',
        'None'
    ], ['RequestsInApplicationQueue', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['CurrentAssemblies', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['TotalAppDomains', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['TotalAppDomainsUnloaded', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Gen0Collections', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Gen1Collections', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Gen2Collections', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['CpuTime', 'total', '0.0', 'seconds', '1536073080', 'PT1M', 'None'],
    ['Requests', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['BytesReceived', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None'],
    ['BytesSent', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None'],
    ['Http101', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Http2xx', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Http3xx', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Http401', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Http403', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Http404', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Http406', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Http4xx', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Http5xx', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['MemoryWorkingSet', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None'],
    ['AverageMemoryWorkingSet', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None'],
    ['AverageResponseTime', 'total', '0.0', 'seconds', '1536073080', 'PT1M', 'None'],
    ['AppConnections', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Handles', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['Threads', 'total', '0.0', 'count', '1536073080', 'PT1M', 'None'],
    ['PrivateBytes', 'total', '0.0', 'bytes', '1536073080', 'PT1M', 'None']
]

discovery = {'': [(u'spo-solutions-fa1', {}), (u'zcldazwamonseas-as', {})]}

checks = {
    '': [(u'spo-solutions-fa1', {
        'cpu_time_percent_levels': (85.0, 95.0),
        'avg_response_time_levels': (1.0, 10.0),
        'error_rate_levels': (0.01, 0.04)
    }, [
        (0, 'Rate of server errors: 0.0', [('error_rate', 0.0, 0.01, 0.04, 0, None)]),
        (0, u'Location: westeurope', []),
        (0, u'CostCenter: 0000252980', []),
        (0, u'ITProduct: C89 Collaboration Platform', []),
        (0, u'OpHours: 7x24', []),
        (0, u'OpLevel: Operation', []),
    ]),
         (u'zcldazwamonseas-as', {
             'cpu_time_percent_levels': (85.0, 95.0),
             'avg_response_time_levels': (1.0, 10.0),
             'error_rate_levels': (0.01, 0.04)
         }, [
             (0, 'CPU time: 0%', [('cpu_time_percent', 0.0, 85.0, 95.0, 0, None)]),
             (0, 'Average response time: 0.00 s', [('avg_response_time', 0.0, 1.0, 10.0, 0, None)]),
             (0, 'Rate of server errors: 0.0', [('error_rate', 0.0, 0.01, 0.04, 0, None)]),
             (0, u'Location: southeastasia', []),
             (0, u'CostCenter: 0000252980', []),
             (0, u'ITProduct: CUV130_MS_IIS (Internet Information Server) Standard', []),
             (0, u'OpHours: 7x24', []),
             (0, u'OpLevel: Operation', []),
         ])]
}
